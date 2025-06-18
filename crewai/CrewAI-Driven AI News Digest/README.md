# 📰 CrewAI News Analysis Agent

This project uses [CrewAI](https://docs.crewai.com/) to create a multi-agent workflow that automates the process of **fetching**, **analyzing**, and **summarizing** the latest news on AI developments using powerful LLMs and vector search.

## 🚀 Features

- 🌐 Searches and stores the latest AI-related news using NewsAPI and ChromaDB
- 🧠 Uses Langchain with Groq (`mixtral-8x7b-32768`) as the LLM
- 🔎 Performs web searches with SerpAPI for context verification
- 📝 Generates detailed reports on AI trends, breakthroughs, and industry implications
- 💾 Saves final summary as a professional report to `ai_news_analysis_2024.txt`

## 🧠 Agent Overview

| Agent | Role | Tools |
|-------|------|-------|
| `News Searcher` | Finds and processes news articles | `News DB Tool` |
| `AI News Writer` | Analyzes, verifies, and summarizes the information | `Get News Tool`, `Web Search Tool` |

## 🛠️ Tools

- **News DB Tool**: Uses NewsAPI to fetch and chunk article content into ChromaDB.
- **Get News Tool**: Retrieves relevant stored documents using semantic search.
- **Web Search Tool**: Queries SerpAPI to retrieve real-time web results.

## 🧱 Requirements

- Python 3.9+
- [NewsAPI](https://newsapi.org/)
- [SerpAPI](https://serpapi.com/)
- [Google Generative AI](https://ai.google.dev/)
- [Groq API](https://console.groq.com/)
- Dependencies listed in `requirements.txt`

## 📦 Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/crewai-news-analysis.git
   cd crewai-news-analysis
Create and activate a virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # For Windows: venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Set up environment variables

Create a .env file in the root directory:

env
Copy
Edit
GROQ_API_KEY=your_groq_api_key
NEWSAPI_KEY=your_newsapi_key
SERPAPI_API_KEY=your_serpapi_key
GOOGLE_API_KEY=your_google_generativeai_key
▶️ Usage
bash
Copy
Edit
python main.py
The agents will:

Search for latest news about AI in 2024

Store and retrieve structured insights using Chroma

Use real-time search to validate facts

Produce a detailed final report with summaries and analysis

Output will be saved in ai_news_analysis_2024.txt.

📁 Project Structure
bash
Copy
Edit
.
├── main.py                    # Main execution script
├── .env                       # Environment variables (not committed)
├── ai_news_analysis_2024.txt  # Output report file
├── chroma_db/                # Local vectorstore database
├── requirements.txt          # Python dependencies
└── README.md                 # You're reading it!
✅ Example Output
Executive Summary

Major AI Trends

Industry-wise Impact

Future Implications

Bullet-point Key Takeaways

🧠 Technologies Used
CrewAI

LangChain

Groq

Google Generative AI Embeddings

ChromaDB

NewsAPI

SerpAPI

💡 Future Enhancements
Add agent memory and planning

Enable auto-updating datasets

Integrate with a front-end dashboard

📜 License
MIT License. See LICENSE file.

Made with ❤️ using CrewAI and LangChain
