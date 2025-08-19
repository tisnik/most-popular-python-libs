from pydantic import BaseModel


class User(BaseModel):
    name: str
    surname: str
    age: int
    registered: bool


user1 = User(name="John", surname="Doe", age=42, registered=False)
print(user1)
