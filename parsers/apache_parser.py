def parse_apache_line(line):
    try:
        parts = line.split(" ")
        return {
            "ip": parts[0],
            "timestamp": parts[3][1:],
            "method": parts[5][1:],
            "path": parts[6],
            "status": parts[8]
        }
    except:
        return None

