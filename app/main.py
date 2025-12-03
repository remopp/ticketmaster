from fastapi import FastAPI
import os
app = FastAPI()

@app.get("/")
def root():
    return {"key": "value"}

@app.get("/config")
def dbs():
        return {"DATABASE_URL" :  os.getenv("DATABASE_URL")}