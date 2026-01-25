import os
from autogen import AssistantAgent, UserProxyAgent
from dotenv import load_dotenv

load_dotenv()

# Pointing to GitHub's free model inference
config_list = [{
    "model": "gpt-4o", # or "gpt-4o-mini"
    "api_key": os.getenv("GITHUB_TOKEN"),
    "base_url": "https://models.inference.ai.azure.com" 
}]

# 1. The Coder: Specialized in Python and Git
coder = AssistantAgent(
    name="Coder",
    llm_config={"config_list": config_list},
    system_message="You are a senior developer. You write Python code to fix GitHub issues. Output only the code blocks."
)

# 2. The Reviewer: Acts as the User Proxy to execute and verify code
reviewer = UserProxyAgent(
    name="Reviewer",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=3,
    is_termination_msg=lambda x: "TERMINATE" in x.get("content", ""),
    code_execution_config={"work_dir": "sandbox", "use_docker": True} 
)

def solve_issue(issue_description):
    reviewer.initiate_chat(coder, message=f"Fix this issue: {issue_description}")