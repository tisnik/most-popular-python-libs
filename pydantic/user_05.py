from pydantic import BaseModel


class User(BaseModel):
    name: str
    surname: str
    age: int | None
    registered: bool = False


user1 = User(name="John", surname="Doe", age=None)
print(user1)
