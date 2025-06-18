from crewai import Agent, Task, Crew, Process
from crewai.tools import BaseTool
from langchain_groq import ChatGroq
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.utilities import SerpAPIWrapper
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from pydantic import BaseModel, Field
from typing import Type
import requests
import os
from dotenv import load_dotenv

# Set USER_AGENT to avoid warning
os.environ['USER_AGENT'] = 'CrewAI-News-Agent/1.0'

# Load API Keys
load_dotenv()

# Google Embedding model
embedding_function = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Groq LLM
llm = ChatGroq(model="mixtral-8x7b-32768", api_key=os.getenv("GROQ_API_KEY"))

# SerpAPI Tool
search_tool = SerpAPIWrapper(serpapi_api_key=os.getenv("SERPAPI_API_KEY"))

# Pydantic models for tool inputs
class NewsSearchInput(BaseModel):
    query: str = Field(..., description="Search query for news articles")

class NewsRetrievalInput(BaseModel):
    query: str = Field(..., description="Query to retrieve news from database")

class WebSearchInput(BaseModel):
    query: str = Field(..., description="Query for web search")

# Tool 1: CrewAI Compatible News Search Tool
class NewsSearchTool(BaseTool):
    name: str = "News DB Tool"
    description: str = "Fetch news articles and store them in ChromaDB database"
    args_schema: Type[BaseModel] = NewsSearchInput

    def _run(self, query: str) -> str:
        """Fetch news articles and store them in ChromaDB."""
        API_KEY = os.getenv('NEWSAPI_KEY')
        if not API_KEY:
            return "NewsAPI key not found. Please set NEWSAPI_KEY in your environment."
        
        base_url = "https://newsapi.org/v2/everything"
        params = {
            'q': query,
            'sortBy': 'publishedAt',
            'apiKey': API_KEY,
            'language': 'en',
            'pageSize': 5,
        }

        try:
            response = requests.get(base_url, params=params)
            if response.status_code != 200:
                return f"Failed to retrieve news. Status code: {response.status_code}"

            articles = response.json().get('articles', [])
            if not articles:
                return "No articles found for the given query."

            all_splits = []
            successful_articles = 0
            article_summaries = []

            for article in articles:
                try:
                    if article.get('url') and article.get('title'):
                        # Store basic article info
                        article_summaries.append({
                            'title': article['title'],
                            'description': article.get('description', ''),
                            'url': article['url'],
                            'published_at': article.get('publishedAt', '')
                        })
                        
                        # Load and process article content
                        loader = WebBaseLoader(article['url'])
                        docs = loader.load()

                        splitter = RecursiveCharacterTextSplitter(
                            chunk_size=1000, 
                            chunk_overlap=200
                        )
                        splits = splitter.split_documents(docs)
                        all_splits.extend(splits)
                        successful_articles += 1
                except Exception as e:
                    print(f"Error processing article {article.get('url', 'Unknown')}: {e}")
                    continue

            if all_splits:
                # Ensure directory exists
                os.makedirs("./chroma_db", exist_ok=True)
                
                # Store in ChromaDB
                vectorstore = Chroma.from_documents(
                    all_splits,
                    embedding=embedding_function,
                    persist_directory="./chroma_db"
                )
                
                # Get sample relevant content
                retriever = vectorstore.similarity_search(query, k=3)
                
                # Format response with article summaries and key points
                result_text = f"Successfully processed {successful_articles} articles about '{query}':\n\n"
                
                # Add article summaries
                for i, article in enumerate(article_summaries, 1):
                    result_text += f"{i}. {article['title']}\n"
                    result_text += f"   Description: {article['description'][:100]}...\n"
                    result_text += f"   Published: {article['published_at']}\n\n"
                
                # Add key content points
                result_text += "Key Content Points Found:\n"
                for i, doc in enumerate(retriever, 1):
                    result_text += f"\nPoint {i}: {doc.page_content[:300]}...\n"
                
                return result_text
            else:
                return f"No content could be extracted from articles about '{query}'. Articles found but content loading failed."
                
        except Exception as e:
            return f"Error fetching news: {str(e)}"

# Tool 2: CrewAI Compatible News Retrieval Tool
class NewsRetrievalTool(BaseTool):
    name: str = "Get News Tool"
    description: str = "Retrieve stored news from ChromaDB database"
    args_schema: Type[BaseModel] = NewsRetrievalInput

    def _run(self, query: str) -> str:
        """Retrieve stored news from ChromaDB."""
        try:
            if not os.path.exists("./chroma_db"):
                return "No news database found. Please run news search first using the News DB Tool."
            
            vectorstore = Chroma(
                persist_directory="./chroma_db", 
                embedding_function=embedding_function
            )
            
            retriever = vectorstore.similarity_search(query, k=5)
            
            if not retriever:
                return f"No relevant news found in database for query: '{query}'. Try a different search term."
            
            result_text = f"Found {len(retriever)} relevant news chunks for '{query}':\n\n"
            for i, doc in enumerate(retriever, 1):
                result_text += f"Result {i}:\n{doc.page_content[:500]}...\n\n"
                result_text += "-" * 50 + "\n\n"
            
            return result_text
            
        except Exception as e:
            return f"Error retrieving news from database: {str(e)}"

# Tool 3: CrewAI Compatible Web Search Tool
class WebSearchTool(BaseTool):
    name: str = "Web Search Tool"
    description: str = "Search the web using SerpAPI for additional information"
    args_schema: Type[BaseModel] = WebSearchInput

    def _run(self, query: str) -> str:
        """Search the web using SerpAPI for additional information."""
        try:
            results = search_tool.run(query)
            return f"Web search results for '{query}':\n{results}"
        except Exception as e:
            return f"Error in web search: {str(e)}"

# Create tool instances
news_search_tool = NewsSearchTool()
news_retrieval_tool = NewsRetrievalTool()
web_search_tool = WebSearchTool()

# Agents
news_search_agent = Agent(
    role='News Searcher',
    goal='Generate key points from the latest news articles about AI developments',
    backstory='You are an expert researcher specializing in AI and technology news. You excel at finding, processing, and organizing the most relevant and current information about AI developments, breakthroughs, and industry trends.',
    tools=[news_search_tool],
    allow_delegation=True,
    verbose=True,
    llm=llm
)

writer_agent = Agent(
    role='AI News Writer',
    goal='Create comprehensive and well-structured summaries from news topics with additional research',
    backstory='You are a skilled technology journalist with expertise in AI and machine learning. You can synthesize information from multiple sources, verify facts through additional research, and create engaging, informative summaries that highlight the most important developments and their implications.',
    tools=[news_retrieval_tool, web_search_tool],
    allow_delegation=True,
    verbose=True,
    llm=llm
)

# Tasks
news_search_task = Task(
    description="""
    Search for the latest news articles about 'AI 2024' and related AI developments.
    Focus on finding articles about:
    - Recent AI breakthroughs and technological advances
    - Major AI company announcements and product launches
    - AI regulation, policy changes, and governance issues
    - AI applications in different industries (healthcare, finance, education, etc.)
    - AI safety and ethical considerations
    - Major AI research publications and findings
    
    Process each article and store the information in the database.
    Generate key points and summaries from each news article found.
    """,
    agent=news_search_agent,
    expected_output="A comprehensive summary of key AI news points from 2024, with articles processed and stored in the database for further analysis."
)

writer_task = Task(
    description="""
    Based on the news articles found and stored in the previous task, create a comprehensive analysis:
    
    Step 1: Identify all topics and themes from the stored news articles
    Step 2: Use the Get News Tool to retrieve detailed information for each major topic
    Step 3: Use the Web Search Tool to find additional context and verify information
    Step 4: Write comprehensive, well-structured summaries for each major development
    
    Your final output should be a professional report including:
    - Executive Summary: Overview of the most significant AI developments in 2024
    - Major Trends Analysis: Detailed breakdown of key trends and patterns
    - Industry Impact: How these developments affect different sectors
    - Future Implications: What these developments mean for the future of AI
    - Key Takeaways: Most important points for stakeholders
    
    Format the report with clear headings, bullet points where appropriate, and ensure it's comprehensive yet readable.
    """,
    agent=writer_agent,
    context=[news_search_task],
    expected_output="A comprehensive, well-structured report on AI developments in 2024 with detailed analysis, industry impact assessment, and future implications."
)

# Crew
news_crew = Crew(
    agents=[news_search_agent, writer_agent],
    tasks=[news_search_task, writer_task],
    process=Process.sequential,
    manager_llm=llm,
    verbose=True
)

# Main execution
if __name__ == "__main__":
    try:
        print("🚀 Starting CrewAI News Analysis...")
        print("=" * 60)
        
        # Check for required API keys
        required_keys = ['GROQ_API_KEY', 'NEWSAPI_KEY', 'SERPAPI_API_KEY', 'GOOGLE_API_KEY']
        missing_keys = [key for key in required_keys if not os.getenv(key)]
        
        if missing_keys:
            print(f"⚠️  Warning: Missing API keys: {', '.join(missing_keys)}")
            print("Some features may not work properly.")
            print()
        
        # Run the crew
        result = news_crew.kickoff()
        
        print("=" * 60)
        print("📋 FINAL ANALYSIS REPORT:")
        print("=" * 60)
        print(result)
        
        # Save result to file
        with open("ai_news_analysis_2024.txt", "w", encoding="utf-8") as f:
            f.write(str(result))
        print("\n💾 Report saved to 'ai_news_analysis_2024.txt'")
        
    except Exception as e:
        print(f"❌ Error running the crew: {str(e)}")
        print("Please check your API keys and internet connection.")