import streamlit as st
import requests

st.title("LangGraph Medical Assistant")
st.caption("Educational use only. Not a real doctor!")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    try:
        res = requests.post("http://localhost:8000/chat", json={"user_input": prompt})
        response = res.json().get("response", "⚠️ Server error")
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)
    except Exception as e:
        st.error(f"Failed: {e}")
