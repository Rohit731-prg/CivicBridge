from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional
from enum import Enum

class Authentication_type(str, Enum):
    police_station = "police_station"
    hospital = "hospital"
    municipality = "municipality"
    panchayat = "panchayat"

class Jurisdiction(BaseModel):
    state: str = Field(...)
    district: str = Field(...)
    municipality: str = Field(...)
    ward_nos: List[int] = []


class AdminModel(BaseModel):
    name: str = Field(..., min_length=1)
    employee_ID: str = Field(..., min_length=4)
    authority_type: Authentication_type = Field(...)
    phone: str = Field(..., min_length=10)
    email: str = Field(...)
    jurisdiction: Jurisdiction   # ✅ Embedded model

    password: str = Field(..., min_length=6)
    is_active: bool = True
    created_at: datetime

class loginModel(BaseModel):
    employee_ID: str = Field(..., min_length=4)
    password: str = Field(..., min_length=6)