from fastapi import FastAPI , Depends
from sqlalchemy.orm import Session
from . import models
from . import crud
from . import schemas
from .database import engine , get_db
import os

models.base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"key": "value"}

@app.post("/users/")
def create_user_endpoint(user: schemas.UserCreate , db: Session = Depends(get_db)):
    db_user = crud.create_user(db= db, user = user )
    return db_user
      
@app.get("/config")
def dbs():
    return {"DATABASE_URL" :  os.getenv("DATABASE_URL")}