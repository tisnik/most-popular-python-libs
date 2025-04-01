"""MCP klient, který přečte obrázek."""


import base64

from PIL import Image as PILImage

from mcp import ClientSession
from mcp.client.sse import sse_client


async def run():
    """Realizace klienta."""
    async with sse_client(url="http://localhost:8000/sse") as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            data = await session.call_tool("house")
            image = PILImage.frombytes('1', (512,512), base64.b64decode(data.content[0].data))
            print(image)
            image.save("house.png")


# přímé spuštění klienta
if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
