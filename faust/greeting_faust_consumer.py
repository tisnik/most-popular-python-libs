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
    "hello-world",
    broker="kafka://localhost:9092",
    value_serializer="raw",
)

greetings_topic = app.topic("greetings")

@app.agent(greetings_topic)
async def greet(greetings):
    async for greeting in greetings:
        print(greeting)


if __name__ == "__main__":
    app.main()
