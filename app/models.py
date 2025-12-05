from sqlalchemy import Column,Integer,String,Boolean,DateTime,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import base


class user(base):
    __tablename__= "users"
    id = Column(Integer, primary_key=True, index = True)
    email = Column(String , unique=True, index= True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean , default=True)
    bookings = relationship("Booking", back_populates="user")

class Venue(base):
    __tablename__= "venues"
    id= Column(Integer, primary_key=True, index = True)
    name= Column(String, index= True)
    location = Column(String)
    capacity = Column(Integer)
    events = relationship("Event", back_populates="venue")

class Event(base):
    __tablename__= "events"
    id=Column(Integer, primary_key=True, index = True)
    name= Column(String, index= True, )
    date = Column(DateTime)
    venue_id = Column(Integer, ForeignKey("venues.id"))
    venue = relationship("Venue", back_populates="events")
    bookings = relationship("Booking", back_populates="event")

class Booking(base):
    __tablename__ = "bookings"
    id=Column(Integer, primary_key=True, index = True)
    user_id = Column(Integer , ForeignKey("users.id"))
    event_id= Column(Integer , ForeignKey("events.id"))
    b_time= Column(DateTime , server_default=func.now())
    user = relationship("user", back_populates="bookings")
    event = relationship("Event",back_populates="bookings")