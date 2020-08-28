from datetime import timedelta

def add(moment: 'datetime.datetime') -> 'datetime.datetime':
    return moment + timedelta(seconds = 1e9)