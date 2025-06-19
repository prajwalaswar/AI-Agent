# CourseLanggraph

This project demonstrates building a chatbot using LangGraph.

## Setup

1.  **Install dependencies:**

2.  *Note: You will need to create a `requirements.txt` file containing the libraries used in your notebook (langgraph, langsmith, langchain, langchain-groq, langchain-community, ipython).*

2.  **Set up API Keys:**

    This project requires API keys for LangSmith and Groq. You can set these in your Colab environment using `google.colab.userdata`. The code assumes you have stored them with the keys `groq_api_key` and `LANGSMITH_API_KEY`.

## Usage

1.  Run the notebook in Google Colab.
2.  Enter your prompts in the input box when prompted.
3.  Type `quit` or `q` to exit the conversation.

## Project Structure

- The core logic for the chatbot is within the Colab notebook.
- The notebook defines the LangGraph state, nodes, and edges to create the conversational flow.

## Dependencies

The project relies on the following libraries:

- `langgraph`
- `langsmith`
- `langchain`
- `langchain-groq`
- `langchain-community`
- `ipython`
