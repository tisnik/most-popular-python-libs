from pydantic import BaseModel, Field, PositiveInt, field_validator


class Address(BaseModel):
    street: str
    house_number: PositiveInt | str
    city: str


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


class Character(BaseModel):
    role: str
    user: User
    address: Address | None = None


character = Character(
    role="Detective",
    user=User(name="Sherlock", surname="Holmes", age=42)
)

as_json = character.model_dump_json(indent=4)
print(as_json)
