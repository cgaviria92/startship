from fastapi import Depends, FastAPI

from app.models import models
from .dependencies.database import SessionLocal, engine

from .dependencies.aut import get_query_token, get_token_header
from .internal import admin
from .routers import items, users,aut

app = FastAPI(#dependencies=[Depends(get_query_token)]
              )
models.Base.metadata.create_all(bind=engine)


app.include_router(users.router)
app.include_router(items.router)
#app.include_router(aut.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    #dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

