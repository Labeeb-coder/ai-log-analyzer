import json

def generate_report(anomalies, patterns):
    report = {
        "anomalies": anomalies,
        "patterns": patterns,
        "total_anomalies": len(anomalies)
    }
    with open("incident_report.json", "w") as f:
        json.dump(report, f, indent=4)
