from langchain_community.llms import Ollama

llm = Ollama(
    model="llama3",
    verbose=True
)

def call_llm(prompt: str) -> str:
     """
    Sends a prompt to the local LLM and returns the generated response.

    Acts as a thin wrapper around the LangChain Ollama client, centralizing
    model invocation and enabling easier logging or future customization.
    """
    return llm.invoke(prompt)
