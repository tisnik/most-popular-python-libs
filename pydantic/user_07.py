from pydantic import BaseModel, PositiveInt, field_validator


class User(BaseModel):
    name: str
    surname: str
    age: PositiveInt | None
    registered: bool = False

    @field_validator("age")
    @classmethod
    def check_age(cls, value):
        if value < 18:
            raise ValueError("You are too young to register")
        return value


user1 = User(name="John", surname="Doe", age=17)
print(user1)
