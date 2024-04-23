import faust

app = faust.App(
    "registrations",
    broker="kafka://localhost:9092",
)


class Registration(faust.Record):
    name: str
    surname: str
    id: int


registrations_topic = app.topic("registrations", key_type=str, value_type=Registration)

@app.timer(interval=5.0)
async def example_sender(app):
    await registrations_topic.send(
        value=Registration("Eliška", "Najbrtová", 4))
    await registrations_topic.send(
        value=Registration("Jenny", "Suk", 3))
    await registrations_topic.send(
        value=Registration("Anička", "Šafářová", 0))
    await registrations_topic.send(
        value=Registration("Sváťa", "Pulec", 3))
    await registrations_topic.send(
        value=Registration("Blažej", "Motyčka", 8))
    await registrations_topic.send(
        value=Registration("Eda", "Wasserfall", 0))
    await registrations_topic.send(
        value=Registration("Přemysl", "Hájek", 10))


if __name__ == "__main__":
    app.main()
