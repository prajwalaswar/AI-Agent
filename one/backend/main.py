from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from backend.rag import RAGSystem
from backend.graph import build_langgraph_executor
import os, json

load_dotenv()

app = FastAPI()
CORS(app, allow_origins=["*"])

vector_db = RAGSystem().setup_rag()
agent_executor = build_langgraph_executor(vector_db)

@app.post("/chat")
async def chat(request: Request):
    try:
        body = await request.json()
        user_input = body.get("user_input", "")
        if not user_input:
            return {"error": "Missing user_input field"}

        output = agent_executor.invoke({"input": user_input})
        return {
            "response": output.get("output", output),
            "disclaimer": "Educational use only. Consult a doctor."
        }
    except Exception as e:
        return {"error": str(e)}
