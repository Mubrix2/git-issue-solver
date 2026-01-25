# git-issue-solver

# 🤖 Autonomous GitHub Issue Solver (Agentic AI)

An end-to-end Agentic AI system that autonomously triages, fixes, and tests GitHub issues using a Multi-Agent architecture.

## 🌟 Key Features
- **Multi-Agent Orchestration**: Powered by Microsoft AutoGen (Coder & Reviewer agents).
- **Secure Sandboxing**: LLM-generated code is executed inside isolated **Docker** containers to prevent system harm.
- **Event-Driven**: Integrated with **FastAPI** to handle GitHub Webhooks in real-time.
- **Self-Healing**: The Reviewer agent provides feedback to the Coder if tests fail, triggering an autonomous fix loop.

## 🚀 Technical Architecture

1. GitHub Webhook triggers `/webhook`.
2. **Coder Agent** analyzes the issue and codebase.
3. **Reviewer Agent** runs the code in a Docker sandbox.
4. If successful, the agent prepares a Pull Request.

## 🛠️ Setup
1. `docker build -t issue-agent .`
2. `docker run -p 8000:8000 --env-file .env issue-agent`