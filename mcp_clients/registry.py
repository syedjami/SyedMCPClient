# This ensures your servers start correctly with the right working directory and environment.

from dataclasses import dataclass
from typing import List

@dataclass
class MCPServerConfig:
    name: str
    command: List[str]

SERVERS = {
    "weather": MCPServerConfig(
        name="weather",
        command=[
            "uv",
            "run",
            "--project",
            "C:/mcp/SYEDMCPSERVER/weather",
            "mcp_weather_server",
        ],
    ),
    "stock": MCPServerConfig(
        name="stock",
        command=[
            "uv",
            "run",
            "--project",
            "C:/mcp/SYEDMCPSERVER/stock",
            "mcp_stock_server",
        ],
    ),
}