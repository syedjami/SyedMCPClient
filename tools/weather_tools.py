from langchain.tools import tool
from mcp_clients.weather_client import get_weather

@tool
def weather(city: str):
    return get_weather(city)