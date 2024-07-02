import faust
#
#  (C) Copyright 2024  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

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
