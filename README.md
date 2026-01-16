# LLM Agent POC – Tool-Aware Assistant

## Author: Daniel Jacob Tonn
## Email: danieljt.djt@gmail.com

This project is a **proof of concept (POC)** of an AI assistant capable of **autonomously deciding** when to respond directly to a question or when to use an **external tool (calculator, time tool)** to obtain an accurate answer.

The main objective is to demonstrate:
- Agentic reasoning,
- LLM integration with tools,
- Architecture clarity,
- Local execution without dependence on paid APIs.

---

## Overview

The system flow is as follows:

1. The user asks a question.
2. The **language model (LLaMA 3)** analyzes the question.
3. The model itself decides:
   - **Answer directly**,
   - **Trigger the calculator**,
   - **Trigger an external API for time queries**.
4. The code executes the action chosen by the model.
5. The final response is returned to the user.

The decision is made by the model via a **controlled prompt**, returning a structured JSON that indicates the action to be taken.

---

## Project Structure
```
llm-agent-poc/
├── app/
│ ├── main.py # Application entry point
│ ├── agent.py # Orchestrates decision and execution
│ ├── llm.py # Interface with LLaMA 3 via Ollama
│ └── calculator.py # External tool (calculator)
│ └── time_tool.py # External tool (time query)
│
├── prompts/
│ └── system.txt # Base prompt that instructs the model
│
├── requirements.in # Project dependencies (simplified)
├── requirements.txt # Project dependencies (using uv)
├── .gitignore 
├── Makefile
└── README.md
```

### File Descriptions

- **main.py**  
  Main interaction loop with the user.

- **agent.py**  
  Responsible for:
  - sending the question to the model,
  - interpreting the JSON response,
  - executing the chosen action (calculator or direct response).

- **llm.py**  
  Encapsulates communication with the LLaMA 3 model running locally via Ollama.

- **calculator.py**  
  Implements the external tool used when the model decides that calculation is necessary.

- **prompts/system.txt**  
  Prompt that defines the agent's behavior and the mandatory response format.

---

## Technologies Used

- Python  
- Ollama (local execution of LLMs)  
- LLaMA 3  
- UV (dependency management)
- LangChain

---

## How to Run the Project

### 1. Install Ollama

```make install-ollama```

If in doubt, follow the official instructions at:  
https://ollama.com

After installing, download the model:
```make install-llama3```

Make sure Ollama is running:

```make check-llama3```

---

### 2. Install Python Dependencies

Create a virtual environment (optional) and install dependencies:

```make install```

---

### 3. Run the Agent

At the root of the project:

```make start```

Type questions in the terminal.  
To exit, use:

```exit```

---

## Example Usage

```
LLM Agent with Tool Use (type 'exit' to quit)

User: What is 50 + 30?
Deciding action...
Using calculator tool
Assistant: The result is: 80

User: What time is it in New York?
Deciding action...
Using time tool
Assistant: 2026-01-16T07:34:09.703782-05:00

User: Tell me about artificial intelligence
Deciding action...
Answering directly
Assistant: Artificial intelligence is... [LLM response]

User: exit
```

---

## Architecture Flow

```
User Input
    ↓
    ├─→ Decision Prompt (via LLaMA 3)
    ↓
JSON Decision Response
    ↓
    ├─→ "calculator" → Execute Calculator Tool
    ├─→ "time_tool" → Execute Time Tool
    └─→ "final" → Direct LLM Response
    ↓
Final Response to User
```

---

## Adding New Tools

To extend the agent with new tools, follow these steps:

1. **Create a new tool file** (e.g., `app/weather_tool.py`):
   ```python
   def get_weather(location: str) -> str:
       """Fetches weather information for a given location."""
       # Implementation here
       return f"Weather in {location}: ..."
   ```

2. **Update the decision prompt** in `prompts/system.txt`:
   ```json
   Weather tool:
   {
     "action": "weather_tool",
     "location": "<location>"
   }
   ```

3. **Import and handle in agent.py**:
   ```python
   from weather_tool import get_weather
   
   if decision.get("action") == "weather_tool":
       return get_weather(decision["location"])
   ```

# What I Learned with This Application
1. How to use the Ollama library to interact with local LLMs. I have only used OpenAI, Gemini, and Deepgram before.
2. I learned about local LLM models.
3. That I really like building agentic applications with LLMs :D 

## General Task Considerations
1. The calculator is implemented as a local Python function using the standard library, ensuring cross-platform compatibility and avoiding OS-specific commands or external services.
2. The LLM model answers better when asked in English, so the prompt and interactions are in English. Portuguese questions may be answered incorrectly.
3. Some `make` commands may not work as expected on Windows systems due to differences in shell environments. These commands were designed to work on Linux systems. Please, if you use Windows, adapt the commands accordingly. See the `Makefile` file to check the commands.
4. An current limitationof this model is about questions that mixes calculation with non-numeric context. For example, if you ask "What is white + black?" the model may not choose the calculator tool, even though the correct answer is "white + black = gray". This can be improved in future iterations.

# Improvements to Be Made
1. We know that sometimes AI can make mistakes, but if you ask the same thing again it may get it right. So we can implement a retry mechanism for the LLM calls.
2. The model may respond slowly sometimes. We can implement caching for repeated questions. Also, this model doesn't work well for questions in Portuguese, so adding translation tools may be efficient.
3. Advanced math questions may not be answered correctly. We can improve the prompt to make the model use the calculator more often for complex math questions. We could also implement an advanced calculator tool using SymPy or a similar library.
4. Add more tools, like a web search tool to get up-to-date information from the internet.
5. Implement a history of interactions to improve context and continuity in conversations.
6. Create a web interface for better user experience instead of command-line interaction.
7. Add unit tests and integration tests to ensure reliability and correctness of the application. Pytest can be used for this purpose.
8. Implement logging to monitor the application's behavior and diagnose issues.

Clearly, all these improvements can be done in future iterations and are very useful, although they require time to implement and should be prioritized according to the project goals.

Have a good day!