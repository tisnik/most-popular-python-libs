"""MCP klient, který spustí server, se kterým se komunikuje přes SSE."""

from mcp import ClientSession
from mcp.client.sse import sse_client


async def run():
    """Realizace klienta."""
    async with sse_client(url="http://localhost:8000/sse") as (read, write):
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
