from pydantic import BaseModel, Field

class ComplainModel(BaseModel):
    user_id: str = Field(..., description="Identifier of the user who filed the complaint")
    address_id: str = Field(..., description="Identifier of the address associated with the complaint")
    title: str = Field(..., description="Title of the complaint")
    description: str = Field(..., description="Detailed description of the complaint")
    status: str = Field(..., description="Current status of the complaint (e.g., open, closed, in-progress)")
    created_at: str = Field(..., description="Timestamp when the complaint was created")
    updated_at: str = Field(..., description="Timestamp when the complaint was last updated")