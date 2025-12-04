from sqlalchemy import Column,Integer,String,Boolean,DateTime,ForeignKey
from sqlalchemy.orm import relationship
from .database import base


class user(base):
    __tablename__= "users"
    id = Column(Integer, primary_key=True, index = True)
    email = Column(String , unique=True, index= True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean , default=True)

class Venue(base):
    __tablename__= "venues"
    id= Column(Integer, primary_key=True, index = True)
    name= Column(String, index= True)
    location = Column(String)
    capacity = Column(Integer)
    events = relationship("Event" , back_populates="venue")

class Event(base):
    __tablename__= "events"
    id=Column(Integer, primary_key=True, index = True)
    name= Column(String, index= True)
    date = Column(DateTime)
    venue_id = Column(Integer, ForeignKey("venues.id"))
    venue = relationship("Venue" , back_populates="events")