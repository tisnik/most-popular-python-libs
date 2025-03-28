"""MCP klient, který přečte zvolený zdroj a získá z něj data."""

from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# parametry pro spuštění MCP serveru
server_params = StdioServerParameters(
    command="python",  # spustí se tento příkaz
    args=["mcp_server_5.py"],  # a předají se mu následující parametry
    env=None,  # lze definovat i proměnné prostředí
)


async def run():
    """Realizace klienta."""
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # přečtení zdroje
            data = await session.read_resource("pozdrav://")
            print("Data returned:", data)
            print("Type:", type(data))

            text = data.contents[0].text
            print("Text:", text)


# přímé spuštění klienta
if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
