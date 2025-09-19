from pydantic import BaseModel, PositiveInt


class User(BaseModel):
    """Model reprezentující uživatele."""
    name: str
    surname: str
    age: PositiveInt | None
    registered: bool = False


user1 = User(name="John", surname="Doe", age=-1)
print(user1)
