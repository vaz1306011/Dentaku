import re


def normalize_operator(expression: list | str) -> str:
    text = "".join(expression)
    text = text.replace("÷", "/")
    text = text.replace("×", "*")
    return text


def display_operator(expression: list | str) -> str:
    def replace_ops(text: str):
        text = text.replace("/", "÷")
        text = text.replace("*", "×")
        return text

    expression = "".join(expression)
    parts = re.split(r"(<[^>]+>)", expression)

    result = []
    for part in parts:
        if part.startswith("<") and part.endswith(">"):
            result.append(part)
        else:
            result.append(replace_ops(part))
    return "".join(result)
