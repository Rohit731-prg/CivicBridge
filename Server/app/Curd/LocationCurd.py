from app.Database.Model.LocationModel import LocationModel
from fastapi import HTTPException
from app.Config.ConnectDb import collection_location

async def setLocationDate(location: LocationModel) -> dict:
    try:
        loc = await collection_location.insert_one(location.dict())
        return { "message": "Location data saved successfully", "location_id": str(loc.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))