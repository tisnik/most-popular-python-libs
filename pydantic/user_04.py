from pydantic import BaseModel


class User(BaseModel):
    """Model reprezentující uživatele."""
    name: str
    surname: str
    age: int
    registered: bool


user1 = User(name="John", surname="Doe", age=None, registered=None)
print(user1)
