from contextlib import asynccontextmanager
from typing import AsyncIterator
from fastmcp import Client
from fastmcp.client.transports import StdioTransport  # Import the explicit transport
from .registry import MCPServerConfig

@asynccontextmanager
async def mcp_client_for_server(cfg: MCPServerConfig) -> AsyncIterator[Client]:
    # Ensure command is in list format for StdioTransport
    cmd_list = cfg.command if isinstance(cfg.command, list) else cfg.command.split()
    
    # Explicitly define the transport instead of letting FastMCP 'infer' it
    # cmd_list[0] is 'uv', cmd_list[1:] is the rest of the arguments
    transport = StdioTransport(command=cmd_list[0], args=cmd_list[1:])
    
    async with Client(transport) as client:
        yield client
