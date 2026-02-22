from fastapi import APIRouter, Response, HTTPException
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
        address = address_details.get("address", {})
        if not address.get("country") == "India":
            raise HTTPException(status_code=404, detail="This software is for Indian residential")

        newRequest_obj = {
            "area_name": address_details.get("display_name", "unknown"),
            "city": address.get("city") 
                or address.get("town") 
                or address.get("village") 
                or "unknown",
            "residential": address.get("residential")
                   or address.get("hamlet") 
                   or "unknown",
            "districts": address.get("state_district") or "unknown",
            "state": address.get("state") or "unknown",
            "country": address.get("country") or "unknown",
            "latitude": location.latitude,
            "longitude": location.longitude,  # FIXED THIS TOO
}
        rewRequest = LocationModel(**newRequest_obj)
        res = await setLocationDate(rewRequest)
        response.status_code = 201
        return res
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e)
)