from fastapi import FastAPI, Request
from agents import solve_issue

app = FastAPI()

@app.post("/webhook")
async def github_webhook(request: Request):
    payload = await request.json()
    
    # Check if a new issue was opened
    if payload.get("action") == "opened":
        issue_body = payload["issue"]["body"]
        # Trigger the agentic workflow
        solve_issue(issue_body)
        return {"status": "Agent started fixing the issue"}
        
    return {"status": "Ignored action"}