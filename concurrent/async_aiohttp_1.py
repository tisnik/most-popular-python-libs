import asyncio
import aiohttp
import time


async def download(name, queue):
    async with aiohttp.ClientSession() as session:
        while not queue.empty():
            url = await queue.get()
            print(f"Task named {name} getting URL: {url}")
            async with session.get(url) as response:
                t = await response.text()
                print(f"Task named {name} downloaded {len(t)} characters")
            print(f"Task named {name} finished")


async def main():
    queue = asyncio.Queue()

    for url in (
        "http://www.root.cz",
        "http://duckduckgo.com",
        "http://seznam.com",
        "https://www.root.cz/programovaci-jazyky/",
        "https://www.root.cz/clanky/soubezne-a-paralelne-bezici-ulohy-naprogramovane-v-pythonu/",
        "https://github.com/",
    ):
        await queue.put(url)

    await asyncio.gather(
        asyncio.create_task(download(1, queue)), asyncio.create_task(download(2, queue))
    )


asyncio.run(main())
