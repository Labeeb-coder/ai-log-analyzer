from collections import Counter

def recognize_patterns(parsed_logs):
    events = [log.get("path") or log.get("message") for log in parsed_logs if log]
    return dict(Counter(events))
