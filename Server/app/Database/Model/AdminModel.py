from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional


class Jurisdiction(BaseModel):
    state: str = Field(...)
    district: str = Field(...)
    municipality: str = Field(...)
    ward_nos: List[int] = []
    police_station_code: Optional[str] = None


class AdminModel(BaseModel):
    name: str = Field(..., min_length=1)
    employee_ID: str = Field(..., min_length=4)
    authority_type: str = Field(..., min_length=1)
    phone: str = Field(..., min_length=10)
    email: str = Field(...)
    jurisdiction: Jurisdiction   # ✅ Embedded model

    password: str = Field(..., min_length=6)
    is_active: bool = True
    created_at: datetime

class loginModel(BaseModel):
    employee_ID: str = Field(..., min_length=4)
    password: str = Field(..., min_length=6)