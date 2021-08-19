from typing import List

from fastapi import Depends, FastAPI, HTTPException
# from sqlalchemy.orm import Session
from passlib.context import CryptContext
# from sqlalchemy.sql.expression import false
# from crud import get_user_by_email,create_user_db,get_users,get_user,create_user_item,get_items,get_user_by_username,get_info_all_users
# from models import Base
# from schemas import User,UserCreate,ItemCreate,Item,User_login,
from schemas import UserCreatetModel,User,create_user
# from database import SessionLocal, engine
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Body, HTTPException, status
from fastapi.encoders import jsonable_encoder
from database import client_asincrono,client_sincrono
from fastapi.security import HTTPBasicCredentials
import json 
from typing import Optional

from fastapi import FastAPI
from bson import ObjectId
from json import dumps
from schematics.models import Model
from schematics.types import StringType, EmailType

# Base.metadata.create_all(bind=engine)



# An instance of class User


# funtion to create and assign values to the instanse of class User created







pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
app = FastAPI()
#db = client.test
db_sy = client_sincrono['usersdata']
db_asy = client_asincrono['usersdata']

#app.router.redirect_slashes = False

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.post("/login/", response_model=User_login)
# async def login(user: User_login, db: Session = Depends(get_db)):
#     db_user = get_user_by_username(db, username=user.username)
#     login_resp = False
#     if db_user != None:
#         login_resp=pwd_context.verify(user.password,db_user.hashed_password)
#     if login_resp==False or db_user == None :
#         raise HTTPException(status_code=404, detail="usuario o contraseña errada")
#     if login_resp==True:
#         info_all_user=get_info_all_users(db, user_id=db_user.id)
#         return(JSONResponse(info_all_user))
#         #return(JSONResponse(content=db_user.id)) 

# @app.post("/users/", response_model=User)
# async def create_user(user: UserCreate, db: Session = Depends(get_db)):
#     db_user = get_user_by_username(db, username=user.username)
#     if db_user:
#         raise HTTPException(status_code=400, detail="User already registered")
#     user.password = pwd_context.hash(user.password)
#     return create_user_db(db=db, user=user)


# @app.get("/users/", response_model=List[User])
# async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = get_users(db, skip=skip, limit=limit)
#     return users


# @app.get("/users/{user_id}", response_model=User)
# async def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


# @app.post("/users/{user_id}/items/", response_model=Item)
# async def create_item_for_user(
#     user_id: int, item: ItemCreate, db: Session = Depends(get_db)
# ):
#     return create_user_item(db=db, item=item, user_id=user_id)


# @app.get("/items/", response_model=List[Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = get_items(db, skip=skip, limit=limit)
#     return items










##login no tocar
# Our root endpoint
@app.get("/")
def index():
    return {"message": "Hello World"}

# Signup endpoint with the POST method
@app.post("/signup/{email}/{username}/{password}")
def signup(email, username: str, password: str):
    user_exists = False
    data = create_user(email, username, password)
    insert_data(data)
    # Covert data to dict so it can be easily inserted to MongoDB
    #dict(data)

    # Checks if an email exists from the collection of users
    if db_sy.users.find(
        {'username': data['username']}
        ).count() > 0:
        user_exists = True
        print("USer Exists")
        return {"message":"User Exists"}
    # If the email doesn't exist, create the user
    elif user_exists == False:
        db_sy.users.insert_one(data)

        logeo=login(username=data['username'],password=data['password'])
        my_json = json.loads(logeo.body)
        return JSONResponse(my_json)

# Login endpoint
@app.get("/login/{username}/{password}")
def login(username, password):
    def log_user_in(creds):
        if creds['username'] == username and creds['password'] == password:
            return {"message": creds['username'] + ' successfully logged in'}
        else:
            return {"message":"Invalid credentials!!"}
    # Read email from database to validate if user exists and checks if password matches
    logger = check_login_creds(username, password)
    if bool(logger) != True:
        if logger == None:
            logger = "Invalid Email"
            return {"message":logger}
    else:
        
        return JSONResponse(logger)


def email_exists(username):
    user_exist = True
    if db_sy.users.find(
        {'username': username}
    ).count() == 0:
        user_exist = False
        return user_exist

def check_login_creds(username, password):
    if not email_exists(username):
        activeuser = db_sy.users.find(
            {'username': username}
        )
        for actuser in activeuser:
            actuser = dict(actuser)
            actuser['_id'] = str(actuser['_id'])    
            return actuser

def insert_data(data):
    data['user_active']=True
    data['location_x']=10
    data['location_y']=10
    data['location_map']=1
    data['money']=1000
    data['exp']=0
    data['hp_current']=100
    data['ship_use']=1
    data['ship_active']=True
    data['bonus_repair_robot']=100
    data['bonus_enhancer_critical']=0
    data['bonus_enhancer_speed']=0
    data['bonus_enhancer_shield']=0
    data['update_hp']=0
    data['update_speed']=0
    data['update_damage']=0
    data['update_critical']=0
    return data
