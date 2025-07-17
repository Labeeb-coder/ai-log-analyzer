def parse_bgl_line(line):
    parts = line.split()
    return {
        "timestamp": parts[0] + " " + parts[1],
        "message": " ".join(parts[2:]),
    }
