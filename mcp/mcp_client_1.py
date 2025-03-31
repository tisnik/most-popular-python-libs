"""MCP klient, který spustí server, se kterým se komunikuje přes STDIO."""

from mcp import ClientSession, StdioServerParameters
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

            prompts = await session.list_prompts()
            print(prompts)

            resources = await session.list_resources()
            print(resources)

            templates = await session.list_resource_templates()
            print(templates)

            tools = await session.list_tools()
            print(tools)


# přímé spuštění klienta
if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
