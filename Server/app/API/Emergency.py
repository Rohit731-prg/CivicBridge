from fastapi import APIRouter, Response, Depends, HTTPException
from app.Middleware.verify import verify
from app.Database.Model.EmergencyModel import Emergency_claim_model, EmergencyModel
from datetime import datetime
from app.Curd.EmergencyCurd import request_emergency, get_all_emergency_byUser
import httpx


router = APIRouter(
    prefix="/api/emergency",
    tags=["Emergency"]
)


@router.post("/claim-emergency")
async def claim_emergency(
    response: Response,
    request: Emergency_claim_model,
    current_user: dict = Depends(verify)
) -> dict:
    try:
        # 🔹 Reverse Geocoding API
        api = (
            f"https://nominatim.openstreetmap.org/reverse"
            f"?format=jsonv2"
            f"&lat={request.latitude}"
            f"&lon={request.longitude}"
            f"&accept-language=en"
        )

        async with httpx.AsyncClient(timeout=10.0) as client:
            geo_response = await client.get(
                api,
                headers={"User-Agent": "Emergency-FastAPI-App"}
            )

        if geo_response.status_code != 200:
            raise HTTPException(
                status_code=502,
                detail="Failed to fetch address details"
            )

        address_details = geo_response.json()

        # 🔹 Emergency payload
        claim_request = {
            "user_id": current_user["_id"],   # ✅ dict access
            "emergency_type": request.emergency_type,
            "latitude": request.latitude,
            "longitude": request.longitude,
            "address_details": dict(address_details),
            "status": "triggered",
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }
        claim_request = EmergencyModel(**claim_request)
        res = await request_emergency(claim_request)

        response.status_code = 201
        return {
            "success": True,
            "message": "Emergency claimed successfully",
            "data": res
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.get("/getAllEmengencyByUserID")
async def get_all_emergency_UserID_router(
    response: Response,
    current_user: dict = Depends(verify)
) -> list:
    try:
        id = current_user["_id"]
        res = await get_all_emergency_byUser(str(id))
        response.status_code = 200
        return res
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
