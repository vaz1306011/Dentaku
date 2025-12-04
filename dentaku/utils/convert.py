def normalize_operator(expression: list | str) -> str:
    text = "".join(expression)
    text = text.replace("÷", "/")
    text = text.replace("×", "*")
    return text
