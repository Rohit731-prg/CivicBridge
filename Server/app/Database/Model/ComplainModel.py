from pydantic import BaseModel, Field
from pydantic.types import Date
from enum import Enum

class containStatus(str, Enum):
    pending = "pending"
    submit = "submit"
    progress = "progress"
    resolve = "resolve"
    reject = "reject"

# class Category(str, Enum):
#     Garbage_and_Cleanliness = "Garbage_and_Cleanliness"
#     Water Supply Problem = "Garbage_and_Cleanliness"
#     Garbage_and_Cleanliness = "Garbage_and_Cleanliness"
#     Garbage_and_Cleanliness = "Garbage_and_Cleanliness"
#     Garbage_and_Cleanliness = "Garbage_and_Cleanliness"

class ComplainModel(BaseModel):
    category: str = Field(..., description="Category of the complaint")
    sub_category: str = Field(..., description="Category of the place")
    user_id: str = Field(..., description="Identifier of the user who filed the complaint")
    address_id: str = Field(..., description="Identifier of the address associated with the complaint")
    title: str = Field(..., description="Title of the complaint")
    description: str = Field(..., description="Detailed description of the complaint")
    evidence: str = Field(..., description="Evidence related to the complaint, such as image or video URL")
    status: containStatus = Field(..., description="Current status of the complaint (e.g., open, closed, in-progress)")
    created_at: Date = Field(..., description="Timestamp when the complaint was created")
    updated_at: Date = Field(..., description="Timestamp when the complaint was last updated")

class Fetch_request_model(BaseModel):
    category: str = Field(..., description="Category of the complaint")
    place: str = Field(..., description="place for the fetching")