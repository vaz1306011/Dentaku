def normalize_operator(expression: list | str) -> str:
    expression_str = "".join(expression).replace("÷", "/").replace("×", "*")
    return expression_str


def display_operator(expression: list | str) -> str:
    expression_str = "".join(expression).replace("/", "÷").replace("*", "×")
    return expression_str
