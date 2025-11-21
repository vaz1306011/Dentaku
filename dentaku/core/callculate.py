import re


def callculate(expr: str):
    if not re.fullmatch(r"[0-9+\-*/().\s]+", expr):
        raise ValueError("Invalid characters in expression")
    return eval(expr)
