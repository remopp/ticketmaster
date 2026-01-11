from sqlalchemy.orm import Session
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError
from .  import models
from . import schemas

pwd_context = CryptContext(schemes= ["bcrypt"], deprecated = "auto")

def create_user(db: Session , user: schemas.UserCreate):
    hashedpass =  pwd_context.hash(user.password)
    db_user = models.user(email=user.email , username = user.username , hashed_password = hashedpass)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_venue(db: Session, venue: schemas.VenueCreate):
    db_venue = models.Venue(name = venue.name , location = venue.location ,  capacity = venue.capacity)
    db.add(db_venue)
    db.commit()
    db.refresh(db_venue)
    return db_venue

def create_event(db: Session , event: schemas.EventCreate):
    if(db.query(models.Event).filter(models.Event.date == event.date , models.Event.venue_id == event.venue_id).first() is not None):
        return None
    try:
        db_event = models.Event(name = event.name , date = event.date, venue_id = event.venue_id)
        db.add(db_event)
        db.commit()
        db.refresh(db_event)
        return db_event
    except IntegrityError:
        db.rollback()
        return None

def book_ticket(db:Session, booking: schemas.BookingCreate):
    event = db.query(models.Event).filter(models.Event.id == booking.event_id).with_for_update().first()
    if(event == None):
        return None
    cap = db.query(models.Booking).filter(models.Booking.event_id == booking.event_id).count()
    if(cap >= event.venue.capacity):
        raise ValueError("venue is fully booked")
    
    db_booking = models.Booking( user_id = booking.user_id , event_id = booking.event_id)
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking