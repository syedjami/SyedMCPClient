# graphs/main_graph.py

from langgraph.graph import StateGraph
from agents.planner import plan
from agents.reflect import reflect
from agents.adapt_retry import adapt_and_retry
from tools.stock_tools import stock_price
from tools.weather_tools import weather


def initial_state(query, city=None, symbol=None):
    return {
        "query": query,
        "city": city,
        "symbol": symbol,
        "tool": None,
        "result": None,
        "status": None,
    }


graph = StateGraph(initial_state)


@graph.node
def planner_node(state):
    tool = plan(state["query"])
    return {"tool": tool}


@graph.node
def tool_node(state):
    tool = state["tool"]

    if tool == "weather":
        return {"result": weather(state.get("city"))}

    if tool == "stock":
        return {"result": stock_price(state.get("symbol"))}

    return {"result": None}


@graph.node
def reflect_node(state):
    status = reflect(state["result"])
    return {"status": status}


@graph.node
def retry_node(state):
    new_params = adapt_and_retry(state["tool"], state)
    return new_params


graph.add_edge("planner_node", "tool_node")
graph.add_edge("tool_node", "reflect_node")
graph.add_conditional_edges(
    "reflect_node",
    {
        "retry": "retry_node",
        "ok": "__end__",
    },
    lambda s: s["status"],
)
graph.add_edge("retry_node", "tool_node")