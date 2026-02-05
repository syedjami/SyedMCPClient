"""
The Agent Cognitive Loop:
Observe → Plan → Act → Reflect → Adapt

This module defines the core reasoning cycle used by the agent.
It is intentionally modular so LangGraph can call each stage as a node.
"""

from agents.planner import plan
from agents.reflect import reflect
from agents.adapt_retry import adapt_and_retry
from tools.stock_tools import stock_price
from tools.weather_tools import weather


def observe(state: dict) -> dict:
    """
    Extracts the relevant information from the user query or previous steps.
    """
    return {
        "query": state.get("query", ""),
        "context": state.get("context", {}),
    }


def decide_tool(query: str) -> str:
    """
    Uses the planner to determine which tool to call.
    """
    return plan(query)


def act(tool_name: str, params: dict):
    """
    Executes the selected tool with the given parameters.
    """
    if tool_name == "weather":
        return weather(params.get("city"))
    if tool_name == "stock":
        return stock_price(params.get("symbol"))
    return None


def cognitive_loop(state: dict) -> dict:
    """
    Full agentic reasoning loop:
    1. Observe
    2. Plan
    3. Act
    4. Reflect
    5. Adapt (if needed)
    """

    # 1. Observe
    obs = observe(state)
    query = obs["query"]

    # 2. Plan
    tool_name = decide_tool(query)

    # Extract parameters from state
    params = {
        "city": state.get("city"),
        "symbol": state.get("symbol"),
    }

    # 3. Act
    result = act(tool_name, params)

    # 4. Reflect
    status = reflect(result)

    # 5. Adapt & Retry
    if status == "retry":
        new_params = adapt_and_retry(tool_name, params)
        result = act(tool_name, new_params)

    return {
        "tool": tool_name,
        "result": result,
        "status": status,
    }