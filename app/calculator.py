import re

def calculate(expression: str) -> str:
    """
    Evaluates a mathematical expression using a restricted and validated syntax.

    Accepts only numeric characters and arithmetic operators to prevent unsafe
    execution, returning an error message when the expression is invalid.
    """
    expression = expression.replace("x", "*")

    if not re.match(r"^[0-9+\-*/(). ]+$", expression):
        return "Invalid expression"

    try:
        return str(eval(expression))
    except Exception:
        return "Calculation error"
