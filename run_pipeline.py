from mcp_tools.log_analyzer import run_log_analysis

if __name__ == "__main__":
    result = run_log_analysis("logs/apache.log")
    print("✅ Analysis complete:")
    print(result)

