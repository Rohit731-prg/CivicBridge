from pydantic import BaseModel, Field

class LocationModel(BaseModel):
    area_name: str = Field(..., min_length=1)
    city: str = Field(..., min_length=1)
    sub_divitions: str = Field(..., min_length=1)
    districts: str = Field(..., min_length=1)
    state: str = Field(..., min_length=1)
    country: str = Field(..., min_length=1)
    latitude: float = Field(...)
    longitude: float = Field(...)