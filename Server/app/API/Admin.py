from fastapi import APIRouter, HTTPException, Response, Depends
from app.Curd.AdminCurd import createAdmin, login
from app.Database.Model.AdminModel import AdminModel, loginModel
from app.Middleware.verify import verify
from app.Utils.hashPassword import generatehash


router = APIRouter(
    prefix="/api/admin",
    tags=["admins"]
)

@router.post("/createAdmin")
async def createAdminRouter(
    response: Response,
    request: AdminModel,
) -> dict:
    try:
        hashPassword = generatehash(request.password)
        newAdmin = dict(request)
        newAdmin["password"] = hashPassword
        res = await createAdmin(dict(newAdmin))

        response.status_code = 201
        return res 

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post("/login")
async def loginRouter(
    response: Response,
    request: loginModel
) -> dict:
    try:
        res = await login(request)
        response.status_code = 200
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))