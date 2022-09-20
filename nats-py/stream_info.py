import asyncio
import nats
from pprint import pprint

URL = "192.168.1.34:44853"
NATS_USERNAME = "local"
NATS_PASSWORD = "--password--"

STREAM_NAMES = ["foo", "bar", "baz"]


async def main():
    print(f"Connecting to NATS at address {URL}")
    nats_connection = await nats.connect(
        URL, user=NATS_USERNAME, password=NATS_PASSWORD
    )
    print("Connected...")

    print("Retrieving JetStream object")
    jet_stream = nats_connection.jetstream()
    print(f"Retrieved {jet_stream}")

    for stream_name in STREAM_NAMES:
        print(f"Stream info for stream {stream_name}:")
        print("-" * 40)

        stream_info = await jet_stream.stream_info(stream_name)
        pprint(stream_info.__dict__)
        print()

    print("Closing connection")
    await nats_connection.close()
    print("Connection closed")


if __name__ == "__main__":
    asyncio.run(main())
