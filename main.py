#from typing import List

from fastapi import FastAPI,Request
from passlib.context import CryptContext

from schemas import User_login,User_register_post
from schemas import create_user,userEntity,User_update
# from database import SessionLocal, engine
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from database import client_asincrono,client_sincrono

import json 

from fastapi import FastAPI
from bson import ObjectId


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




@app.put("/users/{id}",  tags=["users"])
async def update_user(id: str, user: User_update):
    user_exc_none=user.dict(exclude_none=True)
    b = db_sy.users.find_one({"_id": ObjectId(id)})
    for variable_json in user_exc_none:
        variable_json
        # print(user_exc_none[variable_json])
        # print(b[variable_json])
        total =user_exc_none[variable_json]+ b[variable_json]
        if variable_json == 'exp':
            user_exc_none.update(exp=total)
        if variable_json == 'money':
            user_exc_none.update(money=total)
        if variable_json == 'hp_current':
            user_exc_none.update(hp_current=total)
        if variable_json == 'bonus_repair_robot':
            user_exc_none.update(bonus_repair_robot=total)
        if variable_json == 'bonus_enhancer_critical':
            user_exc_none.update(bonus_enhancer_critical=total)
        if variable_json == 'bonus_enhancer_speed':
            user_exc_none.update(bonus_enhancer_speed=total)
        if variable_json == 'bonus_enhancer_shield':
            user_exc_none.update(bonus_enhancer_shield=total)
        if variable_json == 'update_hp':
            user_exc_none.update(update_hp=total)
        if variable_json == 'update_speed':
            user_exc_none.update(update_speed=total)
        if variable_json == 'update_damage':
            user_exc_none.update(update_damage=total)
        if variable_json == 'update_critical':
            user_exc_none.update(update_critical=total)
        else:
            return"paila eso no existe"
        #user_exc_none.update(variable_json=total)
    db_sy.users.update({
        "_id": ObjectId(id)
    }, {
        "$set": dict(user_exc_none)
    })
    x= db_sy.users.find_one({"_id": ObjectId(id)})
    return userEntity(x)











##login no tocar
# Our root endpoint
@app.get("/")
def index():
    return {"message": "Hello World"}

# Signup endpoint with the POST method
@app.post("/signup/")
def signup(User_new:User_register_post):
    user_exists = False
    data = create_user(User_new.email, User_new.username, User_new.password)
    insert_data(data)
    if db_sy.users.find(
        {'username': data['username']}
        ).count() > 0:
        user_exists = True
        print("USer Exists")
        return {"message":"User Exists"}
    # If the email doesn't exist, create the user
    elif user_exists == False:
        db_sy.users.insert_one(data)

        logeo=login(User_new)
        my_json = json.loads(logeo.body)
        return JSONResponse(my_json)

# Login endpoint
@app.post("/login",response_model=User_login)
def login(User :User_login):
    def log_user_in(creds):
        if creds['username'] == User.username and creds['password'] == User.password:
            return {"message": creds['username'] + ' successfully logged in'}
        else:
            return {"message":"Invalid credentials!!"}
    # Read email from database to validate if user exists and checks if password matches
    logger = check_login_creds(User.username, User.password)
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
