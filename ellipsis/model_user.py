from pydantic import BaseModel, Field, PositiveInt, field_validator


class User(BaseModel):
    """Model reprezentující uživatele."""
    name: str = Field(..., max_length=10)
    surname: str = Field(..., max_length=10)
    age: PositiveInt | None
    registered: bool = False

    @field_validator("age")
    @classmethod
    def check_age(cls, value):
        """Kontrola, jestli je uživatel dospělý."""
        if value < 18:
            raise ValueError("You are too young to register")
        return value


user1 = User(name="Nabuchodonozor", surname="II", age=18)
print(user1)
