from fastapi import HTTPException, APIRouter, Response, Form, UploadFile, Depends
from app.Curd.ComplainCurd import request_complain_data, get_complain_by_user, updateStatus
from app.Utils.uploadImage import uploadImage
from typing import List
from app.Middleware.verify import verify

router = APIRouter(
    prefix="/api/complain",
    tags=["Complain"]
)

@router.post("/request-complain")
async def request_complain_router(
    response: Response,
    user_id: str = Form(...),
    address_id: str = Form(...),
    title: str = Form(...),
    description: str = Form(...),
    evidence: UploadFile = Form(...),
    category: str = Form(...)
) -> dict:
    try:
        imageData = await uploadImage(evidence)
        url = imageData["url"]
        complain = {
            "user_id": user_id,
            "address_id": address_id,
            "title": title,
            "description": description,
            "evidence": url,
            "category": category
        }
        res = await request_complain_data(complain)
        response.status_code = 201
        return res
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@router.get("/getAllComplainsByUser")
async def getAllComplainsByUser(
    response: Response,
    current_user: dict = Depends(verify),
) -> list:
    try:
        user_id = str(current_user.get("_id"))
        complains = await get_complain_by_user(user_id)
        response.status_code = 200
        return complains
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    


@router.put("/updateStatus")
async def update_status_router(
    response: Response,
    complain_id: str,
    status: str,
    current_user: dict = Depends(verify),
) -> dict:
    try:
        res = await updateStatus(complain_id, status)
        response.status_code = 200
        return res
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))