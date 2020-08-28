from datetime import datetime

def add(moment):
    return datetime.fromtimestamp(datetime.timestamp(moment) + 1e9)
