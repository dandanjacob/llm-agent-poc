import re
from simpleeval import simple_eval


def calculate(expression: str) -> str:
    """
    Evaluates a mathematical expression using a restricted and validated syntax.

    Uses simpleeval for safe evaluation without the risks of eval(), and accepts
    only numeric characters and arithmetic operators to prevent execution of
    malicious code, returning an error message when the expression is invalid.
    """
    expression = expression.replace("x", "*")

    if not re.match(r"^[0-9+\-*/(). ]+$", expression):
        return "Invalid expression"

    try:
        return str(simple_eval(expression))
    except Exception:
        return "Calculation error"
