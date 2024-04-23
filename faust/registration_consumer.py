import faust

app = faust.App(
    "registrations",
    broker="kafka://localhost:9092",
    #value_serializer="json",
)


class Registration(faust.Record):
    name: str
    surname: str
    id: int


registrations_topic = app.topic("registrations", key_type=str, value_type=Registration)

@app.agent(registrations_topic)
async def register(registrations):
    async for registration in registrations:
        print(f"Registration: {registration}")


if __name__ == "__main__":
    app.main()
