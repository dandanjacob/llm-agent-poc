import json
from llm import call_llm
from calculator import calculate
from time_tool import get_time

DECISION_PROMPT = open("prompts/system.txt").read()

def run_agent(user_input: str) -> str:
     """
    Orchestrates the agent flow by deciding whether to use a tool or answer directly.

    Sends the user input to a decision-only LLM prompt, executes the selected tool
    (calculator or time tool) when required, or falls back to a direct LLM response.
    """
    print("Deciding action...")

    decision_prompt = f"{DECISION_PROMPT}\n\nUser question: {user_input}"
    decision_raw = call_llm(decision_prompt)

    decision = safe_json_load(decision_raw)

    if decision["action"] == "calculator":
        print("Using calculator tool")
        return f"The result is: {calculate(decision['expression'])}"

    if decision["action"] == "time_tool":
        print("Using time tool")
        return get_time(decision["location"])

    print("Answering directly")
    return call_llm(user_input)

def safe_json_load(text: str) -> dict | None:
    """
    Safely parses a JSON string returned by the LLM.

    Returns a dictionary if the JSON is valid, otherwise returns None to prevent
    agent crashes caused by malformed model outputs.
    """
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return None
