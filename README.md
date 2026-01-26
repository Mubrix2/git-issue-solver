# 🤖 Autonomous GitHub Issue Solver (Agentic AI)

An end-to-end Multi-Agent System (MAS) that autonomously triages, fixes, and verifies GitHub issues using a **Self-Healing** code loop.

---

## 📺 Project Demo 

<p>
  <video src="./asset/demo.mp4" width="100%" controls autoplay loop muted></video>
</p>

## 🏗️ System Architecture

This project implements a **Microservices Architecture** to ensure scalability and security.

1. **Transport Layer**: FastAPI endpoint listens for GitHub Webhooks.
2. **Orchestration Layer**:
* **Coder Agent**: Analyzes codebase and proposes Python fixes.
* **Reviewer Agent**: Validates logic and runs test scripts.


3. **Security Layer (The Sandbox)**: All LLM-generated code is executed inside isolated **Docker Containers** using Docker-in-Docker (DinD) patterns.
4. **Observability Layer**: A Streamlit dashboard provides a "Control Tower" view of agent reasoning and logs.

---

## 🛠️ Tech Stack

* **AI Engine**: GPT-4o / GPT-4o-mini (via GitHub Models API)
* **Agent Framework**: Microsoft AutoGen (AG2)
* **Backend**: FastAPI & Uvicorn
* **Frontend**: Streamlit
* **DevOps**: Docker & Docker Compose

---

## 🚀 Getting Started

### 1. Prerequisites

* Docker Desktop installed and running.
* A GitHub Personal Access Token (for the GitHub Models API).

### 2. Environment Setup

Create a `.env` file in the root directory:

```bash
GITHUB_TOKEN=your_github_token_here
AUTOGEN_USE_DOCKER=True

```

### 3. Run with Docker Compose

One command to spin up the entire ecosystem:

```bash
docker compose up --build

```

* **FastAPI**: `http://localhost:8000`
* **Dashboard**: `http://localhost:8501`

---

## 🛡️ Engineering Best Practices

* **Self-Healing Loops**: If the Reviewer detects a crash, it provides the stack trace back to the Coder for an iterative fix.
* **Container Isolation**: Prevents "Prompt Injection" attacks from executing malicious code on the host machine.
* **Dependency Pinning**: Uses a strictly versioned `requirements.txt` to prevent environment drift.

---

## 📂 Project Structure

```text
├── .github/          # CI/CD Workflows
├── sandbox/          # Isolated directory for AI code execution
├── main.py           # FastAPI Webhook Entrypoint
├── agents.py         # Multi-Agent Logic & Configuration
├── dashboard.py      # Streamlit Observability UI
├── Dockerfile        # API Container Blueprint
├── docker-compose.yml# Multi-service Orchestrator
└── requirements.txt  # Pinned Dependencies
