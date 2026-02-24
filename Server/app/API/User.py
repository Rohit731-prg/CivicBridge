from fastapi import APIRouter, Form, Response, HTTPException, UploadFile
from app.Config.ConnectDb import collection_user, collection_location
from app.Utils.hashPassword import generatehash
import random
from app.Utils.uploadImage import uploadImage
from app.Curd.UserCurd import signUp, authentication, login
from app.Database.Model.UserModel import UserModel, SignupModel
from bson import ObjectId

router = APIRouter(
    prefix="/api/user",
    tags=["User"]
)

@router.post("/signup")
async def signUpRoute(
    response: Response,
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    password: str = Form(...),
    address: str = Form(...),
    image: UploadFile = Form(...)
) -> dict:
    try:
        # Validate input first
        signup_data = SignupModel(
            name=name,
            email=email,
            phone=phone,
            password=password,
            address=address
        )

        is_exist = await collection_user.find_one({"email": signup_data.email})
        if is_exist:
            raise HTTPException(status_code=400, detail="User already exist")

        is_location_exist = await collection_location.find_one({ "_id": ObjectId(address) })
        print(is_location_exist, "Address: ", address)
        if not is_location_exist:
            raise HTTPException(status_code=400, detail="Location is not found in database")
        
        # Upload image
        imageURL = await uploadImage(image.file)

        hashedPassword = generatehash(signup_data.password)
        otp = str(random.randint(1000, 9999))

        newUser = {
            "name": signup_data.name,
            "email": signup_data.email,
            "phone": signup_data.phone,
            "password": hashedPassword,
            "auth": False,
            "otp": otp,
            "image": imageURL["url"],
            "address": signup_data.address
        }

        res = await signUp(UserModel(**newUser))
        response.status_code = 201
        return res

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.put("/authentication")
async def authenticationRoute(
    response: Response,
    email: str = Form(...),
    otp: str = Form(...)
) -> dict:
    try:
        res = await authentication(email, otp)
        response.status_code = 200
        return res
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.post("/login")
async def loginRoute(
    response: Response,
    email: str = Form(...),
    password: str = Form(...)
) -> dict:
    try:
        res = await login(email, password)
        response.status_code = 200
        return res
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))