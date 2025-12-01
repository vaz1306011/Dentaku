import re


def normalize_operator(expression: list | str) -> str:
    expression_str = "".join(expression).replace("÷", "/").replace("×", "*")
    return expression_str


# def display_operator(expression: list | str) -> str:

#     expression_str = "".join(expression).replace("/", "÷").replace("*", "×")
#     return expression_str


def display_operator(html):
    def replace_ops(text):
        return text.replace("/", "÷").replace("*", "×")

    html = "".join(html)
    parts = re.split(r"(<[^>]+>)", html)

    result = []
    for part in parts:
        if part.startswith("<") and part.endswith(">"):
            result.append(part)
        else:
            result.append(replace_ops(part))
    return "".join(result)
