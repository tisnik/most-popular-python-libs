from pydantic import BaseModel


class User(BaseModel):
    """Model reprezentující uživatele."""
    name: str
    surname: str
    age: int
    registered: bool


user1 = User()
print(user1)
