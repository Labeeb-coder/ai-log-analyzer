def parse_hdfs_line(line):
    parts = line.split()
    return {
        "component": parts[2] if len(parts) > 2 else "",
        "content": " ".join(parts[4:]),
    }
