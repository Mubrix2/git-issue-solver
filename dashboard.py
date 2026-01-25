import streamlit as st
import requests

st.set_page_config(page_title="Agentic Issue Solver Monitor", layout="wide")

st.title("🤖 Agentic AI: GitHub Issue Solver")
st.sidebar.header("Configuration")

# Allow the user to manually trigger a test issue
repo_url = st.sidebar.text_input("GitHub Repo URL")
issue_text = st.text_area("Simulate an Issue Description")

if st.button("Trigger Agent"):
    with st.spinner("Agent is analyzing and fixing..."):
        # This calls your FastAPI backend
        response = requests.post("http://localhost:8000/webhook", json={
            "action": "opened",
            "issue": {"body": issue_text}
        })
        st.success(response.json()["status"])

st.subheader("Agent Thought Logs")
# In a real setup, you'd stream logs from your Docker container here
st.info("Waiting for agent activity...")