from ast import List
from app.Database.Model.ComplainModel import ComplainModel
from fastapi import HTTPException
from app.Config.ConnectDb import collection_complain
from datetime import datetime
from typing import List, Dict, Any
from bson import ObjectId

async def request_complain_data(complain: dict) -> dict:
    try:
        complainDetails = {
            "user_id": complain["user_id"],
            "address_id": complain["address_id"],
            "title": complain["title"],
            "description": complain["description"],
            "evidence": complain["evidence"],
            "status": "pending",
            "created_at": str(datetime.utcnow()),
            "updated_at": str(datetime.utcnow()),
            "category": complain["category"]
        }
        await collection_complain.insert_one(ComplainModel(**complainDetails))
        return {"message": "Complain data inserted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

    
async def get_complain_by_user(user_id: str) -> List[Dict[str, Any]]:
    try:
        cursor = collection_complain.aggregate([
            {"$match": {"user_id": user_id}},
            {"$lookup": {
                "from": "addresses",
                "localField": "address_id",
                "foreignField": "_id",
                "as": "address_info"
            }},
            {"$unwind": "$address_info"},
            {"$project": {
                "_id": 1,
                "user_id": 1,
                "title": 1,
                "description": 1,
                "evidence": 1,
                "status": 1,
                "category": 1,
                "created_at": 1,
                "updated_at": 1,
                "address": "$address_info"
            }}
        ])

        compiles = await cursor.to_list(length=None)
        return compiles

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



async def updateStatus(complain_id: str, status: str) -> dict:
    try:
        compile = await collection_complain.find_one({ "_id": ObjectId(complain_id) })
        if not compile:
            raise HTTPException(status_code=400, detail="No Complain found")
        
        if compile["status"] != status:
            raise HTTPException(status_code=400, detail="Same status is not applecable")
        
        await collection_complain.find_one_and_update({"_id": ObjectId(complain_id) } , { "$set": { "status": status}})
        return { "message": "Complain Status updated successfully" }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    


