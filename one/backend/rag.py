import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from backend.tools.logger import InteractionLogger

load_dotenv()

class SafeGoogleEmbeddings(GoogleGenerativeAIEmbeddings):
    def embed_documents(self, texts):
        return [list(vec) for vec in super().embed_documents(texts)]

    def embed_query(self, text):
        return list(super().embed_query(text))

class RAGSystem:
    def __init__(self):
        self.embeddings = SafeGoogleEmbeddings(model="models/embedding-001")
        self.logger = InteractionLogger()

    def setup_rag(self):
        loader = PyPDFLoader("data/nephrology_reference.pdf")
        pages = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        docs = text_splitter.split_documents(pages)

        vector_db = Chroma.from_documents(
            documents=docs,
            embedding=self.embeddings,
            persist_directory="./chroma_db"
        )

        self.logger.log("RAG", "init", {"chunks": len(docs)})
        return vector_db
