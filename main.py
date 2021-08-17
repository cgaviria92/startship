from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from sqlalchemy.sql.expression import false
from crud import get_user_by_email,create_user_db,get_users,get_user,create_user_item,get_items,get_user_by_username,get_info_all_users
from models import Base
from schemas import User,UserCreate,ItemCreate,Item,User_login
from database import SessionLocal, engine
from fastapi.responses import JSONResponse


Base.metadata.create_all(bind=engine)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/login/", response_model=User_login)
async def login(user: User_login, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, username=user.username)
    login_resp = False
    if db_user != None:
        login_resp=pwd_context.verify(user.password,db_user.hashed_password)
    if login_resp==False or db_user == None :
        raise HTTPException(status_code=200, detail="usuario o contraseña errada")
    if login_resp==True:
        info_all_user=get_info_all_users(db, user_id=db_user.id)
        return(JSONResponse(info_all_user))
        #return(JSONResponse(content=db_user.id)) 

@app.post("/users/", response_model=User)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")
    user.password = pwd_context.hash(user.password)
    return create_user_db(db=db, user=user)


@app.get("/users/", response_model=List[User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=Item)
async def create_item_for_user(
    user_id: int, item: ItemCreate, db: Session = Depends(get_db)
):
    return create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=List[Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = get_items(db, skip=skip, limit=limit)
    return items
