# agents/adapt_retry.py

def adapt_and_retry(tool_name: str, params: dict) -> dict:
    """
    Adjust parameters for a retry attempt.
    """
    new_params = params.copy()

    if tool_name == "weather" and new_params.get("city"):
        new_params["city"] = new_params["city"].title()

    if tool_name == "stock" and new_params.get("symbol"):
        new_params["symbol"] = new_params["symbol"].upper()

    return new_params