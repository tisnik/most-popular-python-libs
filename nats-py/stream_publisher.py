import asyncio
import nats

URL = "192.168.1.34:44853"
NATS_USERNAME = "local"
NATS_PASSWORD = "--password--"

SUBJECT_NAME = "bar"


async def main():
    print(f"Connecting to NATS at address {URL}")
    nats_connection = await nats.connect(
        URL, user=NATS_USERNAME, password=NATS_PASSWORD
    )
    print("Connected...")

    print("Retrieving JetStream object")
    jet_stream = nats_connection.jetstream()
    print(f"Retrieved {jet_stream}")

    print("Publishing message to stream")
    ack = await jet_stream.publish(f"{SUBJECT_NAME}", b"Hello from Python!")
    print(f"Published and acked: stream={ack.stream}, sequence={ack.seq}")

    print("Closing connection")
    await nats_connection.close()
    print("Connection closed")


if __name__ == "__main__":
    asyncio.run(main())
