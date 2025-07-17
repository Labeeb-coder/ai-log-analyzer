def detect_anomaly(log_line):
    return "500" in log_line or "error" in log_line.lower()
