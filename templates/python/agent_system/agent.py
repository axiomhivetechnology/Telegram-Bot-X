import json
import operator
from typing import Annotated, Sequence, TypedDict, Union
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage, HumanMessage, ToolMessage
from langchain_core.tools import tool
from langgraph.graph import StateGraph, END
from dotenv import load_dotenv
import os

load_dotenv()

# --- Tool Definitions ---

@tool
def get_system_load():
    """Returns the current simulated system load."""
    return "System load is 25% CPU, 40% RAM. All services operational."

@tool
def query_database(query: str):
    """Queries the internal user database for information."""
    # Simulated database retrieval
    return f"Database result for '{query}': Record not found. Please specify more parameters."

tools = [get_system_load, query_database]
tool_executor = {t.name: t for t in tools}

# --- Agent State Definition ---

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]

# --- Node Definitions ---

model = ChatOpenAI(
    model="gpt-4",
    streaming=True,
    api_key=os.getenv("OPENAI_API_KEY") or "dummy_key"
).bind_tools(tools)

def call_model(state):
    messages = state['messages']
    response = model.invoke(messages)
    return {"messages": [response]}

def call_tool(state):
    last_message = state['messages'][-1]
    tool_calls = last_message.tool_calls
    results = []
    for t in tool_calls:
        print(f"Executing tool: {t['name']}")
        tool_obj = tool_executor[t['name']]
        output = tool_obj.invoke(t['args'])
        results.append(ToolMessage(tool_call_id=t['id'], content=str(output)))
    return {"messages": results}

def should_continue(state):
    last_message = state['messages'][-1]
    if not last_message.tool_calls:
        return "end"
    return "continue"

# --- Graph Construction ---

workflow = StateGraph(AgentState)

workflow.add_node("agent", call_model)
workflow.add_node("action", call_tool)

workflow.set_entry_point("agent")

workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "continue": "action",
        "end": END
    }
)

workflow.add_edge("action", "agent")

agent_app = workflow.compile()

# --- Implementation Example ---

if __name__ == "__main__":
    inputs = {"messages": [HumanMessage(content="Check the system load and search the database for user 'Alice'.")]}
    for output in agent_app.stream(inputs):
        for key, value in output.items():
            print(f"Output from node '{key}':")
            print("---")
            print(value)
        print("\n---\n")
