from pydantic import BaseModel, Field
class User(BaseModel):
    id: int = Field(..., description="The unique identifier for a user")
    name: str = Field(..., description="The name of the user")
    email: str = Field(..., description="The email address of the user")

user = User(id=1, name="John Doe 1", email="john.doe@example.com")
print(user)