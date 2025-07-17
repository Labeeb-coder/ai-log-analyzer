from collections import Counter

def analyze_logs(logs):
    patterns = Counter(logs)
    anomalies = [line for line, count in patterns.items() if count < 5]
    return {
        "status": "done",
        "anomalies": len(anomalies),
        "patterns": dict(patterns.most_common(30))
    }
