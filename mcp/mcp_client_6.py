"""MCP klient, který přečte zvolený zdroj a získá z něj strukturovaná data."""

import json
from pprint import pprint

from mcp import ClientSession
from mcp.client.sse import sse_client


async def run():
    """Realizace klienta."""
    async with sse_client(url="http://localhost:8000/sse") as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # přečtení zdroje
            data = await session.read_resource("author://john-doe")
            print("Data returned:", data)
            print("Type:", type(data))

            text = data.contents[0].text
            print("Text:", text)

            deserialized = json.loads(text)
            print("Deserialized:")
            pprint(deserialized)


# přímé spuštění klienta
if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
