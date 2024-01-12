def answer(question):
    tokens = clean_question(question).split()
    previous = extract_operation('noop', 0)

    for i, token in enumerate(tokens):
        if i % 2 == 0:
            previous = previous(extract_number(token))
        else:
            previous = extract_operation(token, previous)

    if not isinstance(previous, int):
        raise ValueError('syntax error')

    return previous


def extract_number(token):
    try:
        return int(token)
    except ValueError:
        raise ValueError('syntax error')


def extract_operation(token, total):
    if not isinstance(total, int):
        raise ValueError('syntax error')

    operations = {
        "plus": lambda x: total + x,
        "minus": lambda x: total - x,
        "divided": lambda x: total // x,
        "multiplied": lambda x: total * x,
        "noop": lambda x: x
    }

    if token not in operations:
        try:
            int(token)
        except ValueError:
            raise ValueError('unknown operation')
        raise ValueError('syntax error')
    return operations[token]


def clean_question(question):
    if not question.lower().startswith('what is'):
        raise ValueError('unknown operation')

    return question.lower().replace("what is", "").replace("?", "").replace(" by", "").strip()
