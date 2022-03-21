import asyncio
import aiohttp
import time


async def download(name, queue, results):
    async with aiohttp.ClientSession() as session:
        while not queue.empty():
            url = await queue.get()
            t1 = time.time()
            print(f"Task named {name} getting URL: {url}")
            async with session.get(url) as response:
                t = await response.text()
                t2 = time.time()
                print(f"Task named {name} downloaded {len(t)} characters in {t2-t1} seconds")
                await results.put(t2-t1)
            print(f"Task named {name} finished")


async def main():
    queue = asyncio.Queue()
    results = asyncio.Queue()

    t1 = time.time()

    for url in (
        "http://www.root.cz",
        "http://duckduckgo.com",
        "http://seznam.com",
        "https://www.root.cz/programovaci-jazyky/",
        "https://www.root.cz/clanky/soubezne-a-paralelne-bezici-ulohy-naprogramovane-v-pythonu/",
        "https://www.root.cz/clanky/pywebio-interaktivni-webove-dialogy-a-formulare-v-cistem-pythonu/",
        "https://streamlit.io/",
        "https://pglet.io/",
        "https://www.root.cz/serialy/graficke-uzivatelske-rozhrani-v-pythonu/",
        "https://github.com/"
    ):
        await queue.put(url)

    await asyncio.gather(
            asyncio.create_task(download(1, queue, results)),
            asyncio.create_task(download(2, queue, results)),
            asyncio.create_task(download(3, queue, results)))

    process_time = 0
    while not results.empty():
        process_time += await results.get()

    print(f"Process time: {process_time} seconds")

    t2 = time.time()
    print(f"Total time:   {t2-t1} seconds")

asyncio.run(main())
