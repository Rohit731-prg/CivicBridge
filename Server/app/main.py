from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.API.User import router as user_router
from app.API.Location import router as location_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # later restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(location_router)