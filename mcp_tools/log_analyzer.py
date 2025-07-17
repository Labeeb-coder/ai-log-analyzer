from parsers.apache_parser import parse_apache_line
from parsers.nginx_parser import parse_nginx_line
from parsers.app_parser import parse_app_line
from anomaly_detector import detect_anomaly
from pattern_recognizer import recognize_patterns
from report_generator import generate_report

def run_log_analysis(filepath):
    logs = []
    anomalies = []

    # Select parser
    if "apache" in filepath:
        parser = parse_apache_line
    elif "nginx" in filepath:
        parser = parse_nginx_line
    else:
        parser = parse_app_line

    with open(filepath) as f:
        for line in f:
            parsed = parser(line)
            if parsed:
                logs.append(parsed)
                if detect_anomaly(line):
                    anomalies.append(parsed)

    patterns = recognize_patterns(logs)
    generate_report(anomalies, patterns)
    return {"status": "done", "anomalies": len(anomalies), "patterns": patterns}
