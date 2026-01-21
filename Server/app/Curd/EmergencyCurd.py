from app.Config.ConnectDb import collection_emergency
from fastapi import HTTPException
from app.Database.Model.EmergencyModel import EmergencyModel
from bson import ObjectId

async def request_emergency(data: EmergencyModel) -> dict:
    try:
        await collection_emergency.insert_one(data)
        return ({ "message": "Request claim successfully "})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

async def get_all_emergency_byUser(id: str) -> list:
    try:
        all_requests = await collection_emergency.find({"_id": ObjectId(id)}).to_list()
        if not all_requests or len(all_requests) == 0:
            raise HTTPException(status_code=400, detail="No records found")
        
        return all_requests
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))