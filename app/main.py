from agent import run_agent

def main():
    """
    Runs a command-line interface loop for interacting with the LLM agent.

    Continuously reads user input, routes it through the agent logic,
    and prints the assistant's response until the user exits.
    """

    print("LLM Agent with Tool Use (type 'exit' to quit)")

    while True:
        user_input = input("\nUser: ")

        if user_input.lower() == "exit":
            break

        response = run_agent(user_input)
        print(f"Assistant: {response}")

if __name__ == "__main__":
    main()
