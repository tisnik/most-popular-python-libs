"""MCP klient, který zavolá nástroj."""

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# parametry pro spuštění MCP serveru
server_params = StdioServerParameters(
    command="go",  # spustí se tento příkaz
    args=["run", "./mcp_server_3.go"],  # a předají se mu následující parametry
    env=None,  # lze definovat i proměnné prostředí
)


async def run():
    """Realizace klienta."""
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            for n in range(11):
                # zavolání nástroje
                data = await session.call_tool("factorial", arguments={"n": n})
                factorial = data.content[0].text
                print(n, factorial)


# přímé spuštění klienta
if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
