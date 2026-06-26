# Modular AI Agent System (Python)

This directory contains a sophisticated implementation of an AI Agent capable of autonomous reasoning and tool execution. It is designed to be integrated as a backend for complex Telegram bot interfaces.

## Technical Architecture
- **Orchestration Layer**: Utilizes `LangGraph` for stateful graph-based orchestration of LLM calls and tool execution.
- **LLM Integration**: Configured for `OpenAI` models using the `LangChain` SDK.
- **Tool-Calling Protocol**: Implements native tool-calling capabilities to interface with external functions and databases.
- **State Management**: Uses a formal `TypedDict` to track the conversation history and tool execution results.

## Implementation Instructions

1.  **Dependency Provisioning**:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Environment Configuration**: Populate the following variables in your `.env` file:
    ```text
    OPENAI_API_KEY=your_openai_api_key_here
    TELEGRAM_TOKEN=your_telegram_token_here
    ```
3.  **Module Integration**:
    The `agent.py` file exports an `agent_app` object which can be imported into your primary Telegram bot script to process complex user queries.

## Integration Example
```python
from agent import agent_app
from langchain_core.messages import HumanMessage

async def handle_user_query(query: str):
    inputs = {"messages": [HumanMessage(content=query)]}
    async for output in agent_app.astream(inputs):
        # Process and route output back to Telegram
        pass
```
