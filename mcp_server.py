from fastapi import FastAPI
from mcp_tools.log_analyzer import run_log_analysis

app = FastAPI()

@app.get("/analyze")
def analyze(filepath: str = "logs/apache.log"):
    return run_log_analysis(filepath)
