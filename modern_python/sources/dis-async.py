import dis
import asyncio


async def say_hello():
    print("Hello world")


async def main():
    t = asyncio.create_task(say_hello())
    await t


asyncio.run(main())

print("say_hello")
dis.dis(say_hello)

print("main")
dis.dis(main)
