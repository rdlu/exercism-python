def response(hey_bob:str) -> str:
    q = hey_bob.strip()
    if is_question(q) and is_yell(q):
        return "Calm down, I know what I'm doing!"
    if is_question(q):
        return "Sure."
    if is_yell(q):
        return "Whoa, chill out!"
    if is_silence(q):
        return "Fine. Be that way!"
    return "Whatever."

def is_question(q:str) -> bool:
    return q.endswith('?')

def is_yell(q:str) -> bool:
    return q.isupper()

def is_silence(q:str) -> bool:
    return q == ''