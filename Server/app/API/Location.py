from fastapi import APIRouter, Response, HTTPException, Form
from app.Curd.LocationCurd import setLocationDate
from app.Database.Model.LocationModel import LocationModel, LocationRequest
import httpx

router = APIRouter(
    prefix="/api/location",
    tags=["Location"]
)

@router.post("/setLocation")
async def setLocationRouter(
    response: Response,
    location: LocationRequest
) -> dict:
    try:
        api = (
            f"https://nominatim.openstreetmap.org/reverse"
            f"?format=jsonv2"
            f"&lat={location.latitude}"
            f"&lon={location.longitude}"
            f"&accept-language=en"
        )

        async with httpx.AsyncClient(timeout=10.0) as client:
            geo_response = await client.get(
                api,
                headers={"User-Agent": "Emergency-FastAPI-App"}
            )

        if geo_response.status_code != 200:
            raise HTTPException(status_code=502, detail="Failed to fetch address details")

        address_details = geo_response.json()

        newRequest_obj = {
            "area_name": "",
            "city": "",
            "sub_divitions": "",
            "districts": "",
            "state": "",
            "country": "",
            "latitude": location.latitude,
            "longitude": location.latitude,
        }
        rewRequest = LocationModel(**newRequest_obj)
        res = await setLocationDate(rewRequest)
        response.status_code = 201
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)
)