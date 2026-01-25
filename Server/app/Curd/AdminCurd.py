from app.Database.Model.AdminModel import loginModel
from fastapi import HTTPException
from app.Config.ConnectDb import collection_admin
from app.Utils.hashPassword import compairPassword
from app.Utils.token import generaytToken

async def createAdmin(admin: dict) -> dict:
    try:
        await collection_admin.insert_one(dict(admin))
        return { "message": "Admin Registerd successfully..!" }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

async def login(request: loginModel) -> dict:
    try:
        admin = await collection_admin.find_one({ "employee_ID": request.employee_ID})
        if not admin or admin == None:
            raise HTTPException(status_code=400, detail="No Employee ID found")
        
        is_password_match = compairPassword(request.password, admin["password"])
        if not is_password_match or is_password_match == False:
            raise HTTPException(status_code=400, detail="Password is wrong")
        
        token = generaytToken(admin)
        return { "token": token, "message": "Login successfully..!", "admin": admin }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

