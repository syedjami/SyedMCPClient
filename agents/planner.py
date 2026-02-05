# agents/planner.py

def plan(query: str) -> str:
    """
    Decide which tool to use based on the query.
    Returns: "weather", "stock", or "none".
    """
    q = query.lower()

    if any(k in q for k in ["weather", "temperature", "forecast"]):
        return "weather"

    if any(k in q for k in ["stock", "price", "market", "share"]):
        return "stock"

    return "none"