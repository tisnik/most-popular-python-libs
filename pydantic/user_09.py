from pydantic import BaseModel, Field, PositiveInt, field_validator


class User(BaseModel):
    name: str = Field(..., max_length=10)
    surname: str = Field(..., max_length=10)
    age: PositiveInt | None
    registered: bool = False

    @field_validator("age")
    @classmethod
    def check_age(cls, value):
        if value < 18:
            raise ValueError("You are too young to register")
        return value


data = """
    {"name": "John",
     "surname": "Doe",
     "age": 18
    }
"""

user1 = User.model_validate_json(data)
print(user1)
