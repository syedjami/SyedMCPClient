# agents/reflect.py

def reflect(result) -> str:
    """
    Evaluate the tool result.
    Returns: "ok" or "retry".
    """
    if result is None:
        return "retry"

    if isinstance(result, dict) and result.get("error"):
        return "retry"

    return "ok"