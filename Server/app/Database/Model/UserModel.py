from pydantic import BaseModel, Field

class UserModel(BaseModel):
    name: str = Field(..., min_length=1)
    email: str = Field(..., min_length=1)
    password: str = Field(..., min_length=1)
    auth: bool = Field(...)
    otp: str = Field(..., min_length=4)
    image: str = Field(...)
    address: str = Field(..., min_length=1)

class LoginModel(BaseModel):
    email: str = Field(..., min_length=1)
    password: str = Field(..., min_length=1)