from pydantic import BaseModel


class User(BaseModel):
    name: str
    surname: str
    age: int
    registered: bool


user1 = User()
print(user1)
