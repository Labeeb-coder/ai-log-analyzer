# log_chatbot.py
from mcp_tools.parser import parse_logs
from mcp_tools.analyzer import analyze_logs
import json

print("🤖 LogBot: Ask about your logs! Type 'exit' to quit.")

# Prompt for log file path
log_file_path = input("You: Enter path to log file: ").strip()

try:
    logs = parse_logs(log_file_path)
except FileNotFoundError:
    print(f"❌ File not found: {log_file_path}")
    exit()

analysis_result = analyze_logs(logs)

while True:
    user_input = input("You: ").strip().lower()
    if user_input == 'exit':
        print("👋 Goodbye!")
        break
    elif user_input == 'anomalies':
        print(f"🚨 Anomalies found: {analysis_result['anomalies']}")
    elif user_input == 'patterns':
        print("📊 Frequent Patterns:")
        for pattern, count in analysis_result['patterns'].items():
            print(f"  {pattern}: {count} times")
    elif user_input == 'show report':
        print("📋 Full Analysis Report:")
        print(json.dumps(analysis_result, indent=2))
    else:
        print("🤖 I can help with 'anomalies', 'patterns', or 'show report'.")

