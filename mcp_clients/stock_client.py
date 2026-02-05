# In stock_client.py
from .base_client import mcp_client_for_server
from .registry import SERVERS

async def get_stock_price(symbol: str):
    cfg = SERVERS["stock"]
    async with mcp_client_for_server(cfg) as client:
        # 1. Change tool name to "get_stock_info" 
        # 2. Use the 'arguments' keyword
        return await client.call_tool("get_stock_info", arguments={"symbol": symbol})
