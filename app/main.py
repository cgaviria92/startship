from datetime import datetime, timedelta
from typing import Optional
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from pydantic import BaseModel
from passlib.context import CryptContext
from app.database.database import SessionLocal, engine, Base
from sqlalchemy.orm import Session
from app.models.user import User, UserCreate 
from app.models.models import UserModel # Importamos UserCreate desde models
from app.security.auth import get_password_hash, verify_password, authenticate_user, create_access_token, get_db,ACCESS_TOKEN_EXPIRE_MINUTES


# Crear todas las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Configuración de la aplicación FastAPI
app = FastAPI()

# Endpoint para crear un usuario
@app.post("/users/", response_model=User)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = get_password_hash(user.password)
    user_obj = UserModel(username=user.username, hashed_password=hashed_password)
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return user_obj



# Endpoint para obtener información de un usuario por su ID
@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Endpoint para obtener información de un usuario por su nombre de usuario
@app.get("/users/", response_model=User)
async def read_user_by_username(username: str, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.username == username).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Endpoint para autenticar usuarios y obtener token de acceso
@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
