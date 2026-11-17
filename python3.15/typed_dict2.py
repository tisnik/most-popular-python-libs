from typing import TypedDict


class User(TypedDict):
    id: int
    name: str
    surname: str


u1: User = {
        "id": 42,
        "name": "John",
        "surname": "Doe",
        "note": "N/A",
        }

print(type(u1))
