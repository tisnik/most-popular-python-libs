from pydantic import BaseModel, Field, PositiveInt, field_validator


class User(BaseModel):
    name: str = Field(..., max_length=10)
    surname: str = Field(..., max_length=10)
    age: PositiveInt | None
    registered: bool = False

    @field_validator("age")
    def check_age(cls, value):
        if value < 18:
            raise ValueError("You are too young to register")
        return value


user1 = User(name="John", surname="Doe", age=18)

as_json = user1.model_dump_json()
print(as_json)

print()

as_json = user1.model_dump_json(indent=4)
print(as_json)
