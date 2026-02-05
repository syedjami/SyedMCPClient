from langchain.tools import tool
from mcp_clients.stock_client import get_stock_price

@tool
def stock_price(symbol: str):
    return get_stock_price(symbol)