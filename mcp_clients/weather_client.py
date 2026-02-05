from .base_client import mcp_client_for_server
from .registry import SERVERS

async def get_weather(city: str):
    cfg = SERVERS["weather"]
    async with mcp_client_for_server(cfg) as client:
        return await client.call_tool("get_weather", {"city": city})