from langchain.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import json, os
from datetime import datetime

class PatientInput(BaseModel):
    name: str = Field(..., description="Full name of patient")

class PatientRetrieverTool(BaseTool):
    name = "patient_retriever"
    description = "Get patient discharge summary by name"
    args_schema: Type[BaseModel] = PatientInput

    def _run(self, name: str):
        with open("data/patients.json") as f:
            patients = json.load(f)
        matches = [p for p in patients if p["patient_name"].lower() == name.lower()]
        return matches[0] if matches else {"error": "Not found"}
