def is_paired(input_string):
    stack = []
    brackets = {"(": ")", "[": "]", "{": "}"}
    for char in input_string:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or char != brackets[stack.pop()]:
                return False
    return not stack
