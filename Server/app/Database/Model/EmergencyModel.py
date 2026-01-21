from pydantic import BaseModel, Field
from enum import Enum
from datetime import date

class emergency_type_enum(str, Enum):
    medical= "medical"
    fire = "fire"
    safety = "safety"
    accident = "accident"

class Status_enum(str, Enum):
    triggered = "triggered"
    assigned = "assigned"
    resolved = "resolved"

class EmergencyModel(BaseModel):
    user_id: str = Field(..., min_length=1)
    emergency_type: emergency_type_enum = Field(...)
    latitude: float = Field(...)
    longitude: float = Field(...)
    address_details: dict = Field(...)
    status: Status_enum = Field(...)
    created_at: date = Field(...)
    updated_at: date = Field(...)

class Emergency_claim_model(BaseModel):
    emergency_type: emergency_type_enum = Field(...)
    latitude: float = Field(...)
    longitude: float = Field(...)