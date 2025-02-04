# Financial Analysis AI Agent

Welcome to the **Financial Analysis AI Agent** project! This repository hosts a cutting-edge AI-driven solution to analyze and summarize stock market data effortlessly. Powered by the **phi** library, this agent combines financial tools and custom utilities to deliver clear and actionable insights.

## 🚀 Features
- **Comprehensive Analysis:** Retrieve stock prices, analyst recommendations, and stock fundamentals.
- **Custom Company Lookup:** Quickly find company symbols using a built-in utility.
- **Easy-to-Understand Output:** Displays data in table format for a polished and professional look.
- **Developer-Friendly:** Debugging and markdown support to make development seamless.

## 📂 Directory Structure
```
├── one.py              # Main script to execute the agent
├── requirements.txt    # Python dependencies
├── README.md           # Documentation
└── .env                # Environment variables (API keys)
```

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- A valid **GROQ API key**

### Steps to Set Up
1. Clone the Repository:
   ```bash
   git clone https://github.com//.git
   cd Financial-Analysis-AI-Agent
   ```
2. Install Dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure the API Key:
   - Create a `.env` file in the project directory.
   - Add your GROQ API key to the file:
     ```
     GROQ_API_KEY=<your_groq_api_key>
     ```
4. Run the Script:
   ```bash
   python one.py
   ```

## 📊 Usage Example

### Command
To compare financial data for specific companies:
```python
agent.print_response(
    "Summarize and compare analyst recommendations and fundamentals for INFY and Phidata. Show in tables.",
    stream=True
)
```

## How It Works
- The Agent uses the **Groq model** (e.g., `llama-3.3-70b-versatile`).
- The **YFinanceTools** fetches real-time market data.
- **Custom instructions** guide the agent to display results in a structured and user-friendly format.

## 🧰 Customization

### Add More Companies
Update the `get_company_symbol` function in `one.py` to include new symbols:
```python
symbols = {
    "NewCompany": "NEW",  # Add more here
}
```

### Integrate New Tools
You can enhance functionality by integrating additional tools into the Agent setup.

## 🔗 Dependencies
- **phi**: Framework for building intelligent agents.
- **python-dotenv**: Manage environment variables easily.

Install them via:
```bash
pip install phi python-dotenv
```

## 🌟 Acknowledgments
Special thanks to the **phi library team** for their innovative tools. Inspired by real-world applications in financial analysis.

## 🤝 Contributions
Contributions are welcome! Feel free to submit a pull request or open an issue if you have suggestions to improve this project.

## 🎯 Future Improvements
- Add **cryptocurrency analysis tools**.
- Incorporate **machine learning models** for trend predictions.
- Enable **multi-language support** for a global audience.

---

Thank you for visiting this repository! If you find this project helpful, don't forget to ⭐ the repo. Let me know if you have any questions or suggestions!

