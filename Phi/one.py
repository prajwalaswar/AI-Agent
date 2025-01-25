
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
# from phi.tools.crypto import CryptoPriceTool
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["GROQ_API_KEY"] = "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"


def get_company_symbol(company: str) -> str:
    """Use this function to get the symbol for a company.

    Args:
        company (str): The name of the company.

    Returns:
        str: The symbol for the company.
    """
    symbols = {
        "Phidata": "MSFT",
        "Infosys": "INFY",
        "Tesla": "TSLA",
        "Apple": "AAPL",
        "Microsoft": "MSFT",
        "Amazon": "AMZN",
        "Google": "GOOGL",
    }
    return symbols.get(company, "Unknown")


agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True), get_company_symbol],
    instructions=[
        "Use tables to display data.",
        "If you need to find the symbol for a company, use the get_company_symbol tool.",
    ],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

agent.print_response(
    "Summarize and compare analyst recommendations and fundamentals for INFY and Phidata. Show in tables.", stream=True
)