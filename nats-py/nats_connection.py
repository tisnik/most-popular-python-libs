import asyncio
import nats

URL = "192.168.1.34:44853"
NATS_USERNAME = "local"
NATS_PASSWORD = "--password--"


async def main():
    print(f"Connecting to NATS at address {URL}")
    nats_connection = await nats.connect(URL, user=NATS_USERNAME, password=NATS_PASSWORD)
    print(f"Connected...{nats_connection}")

    print("Closing connection")
    await nats_connection.close()
    print("Connection closed")


if __name__ == '__main__':
    asyncio.run(main())
