# A quick sanity test.

import asyncio

from mcp_clients.weather_client import get_weather
from mcp_clients.stock_client import get_stock_info


async def main():
    print("Testing weather...")
    print(await get_weather("Austin"))

    print("Testing stock...")
    print(await get_stock_info("AAPL"))


if __name__ == "__main__":
    asyncio.run(main())