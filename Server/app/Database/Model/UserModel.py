from pydantic import BaseModel, Field, EmailStr, field_validator
import re

class UserModel(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailStr
    phone: str = Field(...)
    password: str = Field(..., min_length=1)
    auth: bool = Field(...)
    otp: str = Field(..., min_length=4)
    image: str = Field(...)
    address: str = Field(..., min_length=1)

    @field_validator("phone")
    @classmethod
    def check_phe(cls, value):
        pattern = r"^[6-9]\d{9}$"
        if not re.match(pattern, value):
            raise ValueError("Invalid Indian phone number")
        return value


class SignupModel(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailStr
    phone: str = Field(...)
    password: str = Field(..., min_length=1)
    image: str = Field(...)
    address: str = Field(..., min_length=1)

    @field_validator("phone")
    @classmethod
    def check_phe(cls, value):
        pattern = r"^[6-9]\d{9}$"
        if not re.match(pattern, value):
            raise ValueError("Invalid Indian phone number")
        return value

class LoginModel(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=1)