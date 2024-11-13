# backend/main.py
from typing import Optional
from fastapi import FastAPI, HTTPException, Depends, Request, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from backend.hashing import Hash
from backend.jwttoken import create_access_token
from backend.oauth import get_current_user
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from backend.models import TokenData  # Import TokenData from models.py

app = FastAPI()

# CORS setup
origins = [
    "http://localhost:3001",  # Update this to match your frontend's address
    "http://localhost:3000",  
    "http://localhost:8080",
    "http://127.0.0.1:3000",  # Add this line
    "http://127.0.0.1:8000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB setup
# mongodb_uri = 'mongodb+srv://manjeet:test1234@cluster0.nbszr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
mongodb_uri = 'mongodb+srv://drethikapila29:biAeOIDp3EaUtGGJ@cluster0.xkvfa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
client = MongoClient(mongodb_uri)
db = client["User"]

# Pydantic Models
class User(BaseModel):
    username: str
    company: str
    password: str

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

@app.get("/")
def read_root(current_user: User = Depends(get_current_user)):
    return {"data": "Hello World"}

@app.post("/register")
def create_user(request: User):
    hashed_pass = Hash.bcrypt(request.password)
    user_object = dict(request)
    user_object["password"] = hashed_pass
    db["users"].insert_one(user_object)
    return {"res": "User created successfully"}

# @app.post("/login")
# def login(request: OAuth2PasswordRequestForm = Depends()):
#     user = db["users"].find_one({"username": request.username})
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No user found with this username")
#     if not Hash.verify(user["password"], request.password):
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Wrong username or password")
    
#     access_token = create_access_token(data={"sub": user["username"]})
#     return {"access_token": access_token, "token_type": "bearer"}

@app.post("/login")
def login(request: Login):
    print(f"Received login request: {request.username}, {request.password}")
    user = db["users"].find_one({"username": request.username})
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No user found with this username")
    if not Hash.verify(user["password"], request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Wrong username or password")
    
    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}

