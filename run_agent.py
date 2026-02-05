# Your top-level entrypoint.

import asyncio
import sys

from agents.simple_agent import run_agent


async def _amain():
    if len(sys.argv) < 2:
        print("Usage: python run_agent.py \"your query\"")
        raise SystemExit(1)

    query = sys.argv[1]
    result = await run_agent(query)
    print("RESULT:")
    print(result)


if __name__ == "__main__":
    asyncio.run(_amain())