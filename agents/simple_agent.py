# A minimal agent that routes queries to the right MCP server.

from mcp_clients.weather_client import get_weather
from mcp_clients.stock_client import get_stock_price


async def run_agent(query: str):
    q = query.lower()

    if "weather" in q:
        city = q.split()[-1]
        return await get_weather(city)

    if "stock" in q or "price" in q:
        symbol = q.split()[-1].upper()
        return await get_stock_price(symbol)

    return {"error": "No matching tool for query"}