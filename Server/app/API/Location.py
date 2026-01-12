from fastapi import APIRouter, Response, HTTPException, Form
from app.Curd.LocationCurd import setLocationDate
from app.Database.Model.LocationModel import LocationModel

router = APIRouter(
    prefix="/api/location",
    tags=["Location"]
)

@router.post("/setLocation")
async def setLocationRouter(
    response: Response,
    location: LocationModel
) -> dict:
    try:
        res = await setLocationDate(location)
        response.status_code = 201
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)
)