from langgraph.graph import StateGraph
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_google_genai import ChatGoogleGenerativeAI
from backend.tools.patient_retriever import PatientRetrieverTool
from backend.tools.web_search import WebSearchTool
from langchain.tools.retriever import create_retriever_tool

class GraphState(dict):
    input: str
    output: str

def build_langgraph_executor(vector_db):
    llm = ChatGoogleGenerativeAI(model="models/chat-bison-001", temperature=0.3)

    retriever_tool = create_retriever_tool(
        retriever=vector_db.as_retriever(),
        name="nephrology_guidelines",
        description="Search nephrology reference materials"
    )

    tools = [PatientRetrieverTool(), WebSearchTool(), retriever_tool]
    agent_node = ToolNode(llm=llm, tools=tools)

    graph = StateGraph(GraphState)
    graph.add_node("agent", agent_node)
    graph.add_conditional_edges("agent", tools_condition)
    graph.set_entry_point("agent")
    graph.set_finish_point("agent")

    return graph.compile()