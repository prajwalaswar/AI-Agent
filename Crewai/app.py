import streamlit as st
from crewai import Crew, Process
from tasks import research_task, write_task
from agents import news_researcher, news_writer
from tools import tool

# Function to initialize Crew and run tasks based on user input
def run_agents(topic):
    # Create the crew with agents and tasks
    crew = Crew(
        agents=[news_researcher, news_writer],
        tasks=[research_task, write_task],
        process=Process.sequential,
    )
    # Run the crew with the given topic
    result = crew.kickoff(inputs={'topic': topic})
    return result

# Streamlit UI for input and displaying output
def display_ui():
    st.set_page_config(page_title="AI Agents - Research & Write", layout="wide")

    # Title of the app
    st.title("AI Agents for Research and Writing")

    # Topic input from user
    st.subheader("Enter the topic you want the agents to explore:")
    topic_input = st.text_input("Topic", value="AI in Healthcare")

    if st.button("Run Agents"):
        # Display loading message while processing
        with st.spinner('Processing your request...'):
            result = run_agents(topic_input)

        # Displaying the results in a neat way
        st.subheader(f"Research on {topic_input}:")
        st.markdown(f"### Research Output: {result['research_task']}")
        
        st.subheader(f"Article on {topic_input}:")
        st.markdown(f"### Article Output: {result['write_task']}")

        # Optionally, add images, charts, or graphs here for a more engaging UI
        st.image("https://via.placeholder.com/500", caption="Related Image", width=500)

# Run the app
if __name__ == "__main__":
    display_ui()
