import asyncio
import nats

URL = "192.168.1.34:44853"
NATS_USERNAME = "local"
NATS_PASSWORD = "--password--"

SUBJECT_NAME = "foo"


async def main():
    print(f"Connecting to NATS at address {URL}")
    nats_connection = await nats.connect(URL, user=NATS_USERNAME, password=NATS_PASSWORD)
    print("Connected...")

    print("Publishing message")
    await nats_connection.publish(SUBJECT_NAME, b"Hello from Python!")
    print("Published")

    print("Closing connection")
    await nats_connection.close()
    print("Connection closed")


if __name__ == '__main__':
    asyncio.run(main())
