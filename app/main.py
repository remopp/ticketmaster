from fastapi import FastAPI , Depends, HTTPException
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

@app.post("/events/")
def create_event_endpoint(event: schemas.EventCreate, db: Session = Depends(get_db)):
    db_event = crud.create_event(db= db, event=event)
    if(db_event is None):
        raise HTTPException(status_code=400 , detail="there is a problem with the data inputed")
    return db_event

@app.post("/venues/")
def create_venue_endpoint(venue: schemas.VenueCreate , db: Session = Depends(get_db)):
    db_venue = crud.create_venue(db=db, venue=venue)
    return db_venue

@app.post("/bookings/")
def create_booking_endpoint(booking : schemas.BookingCreate , db: Session = Depends(get_db)): 
    try:
        db_booking = crud.book_ticket(db=db, booking=booking)
        if(db_booking is None):
            raise HTTPException(status_code=400, detail="event does not exist")
        return db_booking 
    except ValueError:
        raise HTTPException(status_code=400, detail="Sold Out")

@app.get("/config")
def dbs():
    return {"DATABASE_URL" :  os.getenv("DATABASE_URL")}