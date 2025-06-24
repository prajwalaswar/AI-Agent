from langchain.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from datetime import datetime

class SearchInput(BaseModel):
    query: str = Field(..., description="Medical question")

class WebSearchTool(BaseTool):
    name = "web_search"
    description = "Search web for medical info"
    args_schema: Type[BaseModel] = SearchInput

    def _run(self, query: str) -> str:
        return f"(Mock) Web search result for: {query}"