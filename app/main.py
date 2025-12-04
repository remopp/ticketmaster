from fastapi import FastAPI
from . import models
from .database import engine
import os

models.base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"key": "value"}

@app.get("/config")
def dbs():
        return {"DATABASE_URL" :  os.getenv("DATABASE_URL")}