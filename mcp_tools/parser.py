def parse_logs(log_file_path):
    with open(log_file_path, 'r') as f:
        lines = f.readlines()
    return lines
