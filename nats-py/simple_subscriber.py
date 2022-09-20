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

    print(f"Subscribing to stream with name '{SUBJECT_NAME}'")
    sub = await nats_connection.subscribe(SUBJECT_NAME)
    print("Subscribed")

    print("Waiting for messages")

    while True:
        message = await sub.next_msg(timeout=100)
        print("Received:", message)

    await nc.close()


if __name__ == '__main__':
    asyncio.run(main())
