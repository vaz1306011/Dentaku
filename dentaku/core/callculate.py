import re


def callculate(expr: str) -> str:
    if not re.fullmatch(r"[0-9+\-*/().\s]+", expr):
        raise ValueError(f"Invalid characters in expression : {expr}")
    if re.fullmatch(r"\d+", expr):
        raise ValueError("Expression must contain at least one operator.")
    try:
        return f"{eval(expr):.8f}".rstrip("0").rstrip(".")
    except ZeroDivisionError:
        return "0"
    except Exception as e:
        return "ERROR"
