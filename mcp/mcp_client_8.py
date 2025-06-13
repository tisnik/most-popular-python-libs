"""MCP klient, který přečte zvolený zdroj a získá z něj data."""

from time import time

from mcp import ClientSession
from mcp.client.sse import sse_client


async def run():
    """Realizace klienta."""
    async with sse_client(url="http://localhost:8000/sse") as (read, write):
        async with ClientSession(read, write) as session:
            t1 = time()
            print("Client initialization")
            print()

            await session.initialize()

            # přečtení zdroje bez selektoru
            data = await session.read_resource("pozdrav://")
            print("Data returned:", data)
            print("Type:", type(data))
            text = data.contents[0].text
            print("Text:", text)
            print()

            # přečtení zdroje se selektorem
            data = await session.read_resource("pozdrav://Pavel")
            print("Data returned:", data)
            print("Type:", type(data))

            text = data.contents[0].text
            print("Text:", text)
            print()

            # zavolání nástroje
            data = await session.call_tool("factorial", arguments={"n": 10})
            factorial = data.content[0].text
            print("10!=", factorial)
            print()

            t2 = time()
            difftime = t2 - t1
            print(f"Client has finished in {difftime} seconds")
            print()


# přímé spuštění klienta
if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
