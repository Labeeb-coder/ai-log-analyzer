def parse_app_line(line):
    try:
        time_part = line.split("]")[0][1:]
        message = line.split("-")[1].strip()
        return {"timestamp": time_part, "message": message}
    except:
        return None
