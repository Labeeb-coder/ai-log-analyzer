# 🧠 AI Log Analyzer

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/API-FastAPI-00A884?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Model: LLaMA 3](https://img.shields.io/badge/Model-LLaMA3-blueviolet?logo=llama)](https://ollama.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> ✨ An AI-powered system for **log file analysis** using local LLaMA3 + FastAPI.  
> 🚨 Detects anomalies, 🧠 recognizes patterns, and 📄 generates automated incident reports.  
> Ideal for **web server logs**, **application logs**, or **custom pipelines**.

---

## 🎯 Features

- 🔍 **Anomaly Detection** – Captures HTTP errors, exceptions, and unusual logs
- 📊 **Pattern Recognition** – Identifies frequent paths/messages
- 🤖 **AI Chatbot Interface** – Interact via terminal CLI using LLaMA3 (Ollama)
- ⚡ **FastAPI REST API** – Query `/analyze` for real-time results
- 📁 **JSON Report Export** – Auto-generated `incident_report.json`

---

<details>
<summary>📁 <strong>Project Structure</strong> (click to expand)</summary>

ai-log-analyzer/
├── main/
│ ├── log_chatbot.py # Interactive CLI chatbot
│ ├── run_pipeline.py # Main execution pipeline
│ ├── llama_query.py # Talk to LLaMA locally
│ ├── mcp_server.py # FastAPI app for RESTful analysis
│ ├── report_generator.py # Saves JSON report
│ ├── anomaly_detector.py # Anomaly rules (500, error)
│ ├── pattern_recognizer.py # Pattern recognition logic
│ └── mcp_tools/
│ ├── parser.py # Raw log parser
│ └── analyzer.py # Combined logic
├── logs/ # Example log files
├── output/ # Generated reports
├── requirements.txt
└── README.md
</details>

---

## ⚙️ Installation

```bash
git clone https://github.com/Labeeb-coder/ai-log-analyzer.git
cd ai-log-analyzer
pip install -r requirements.txt
