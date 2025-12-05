from pydantic import BaseModel
from datetime import datetime
from pydantic import field_validator



class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class VenueCreate(BaseModel):
    name:str
    location:str
    capacity:int

class EventCreate(BaseModel):
    name:str
    date: datetime
    venue_id:int
    @field_validator('date')
    def check_date(cls , v):
        if(v < datetime.now()):
            raise ValueError("the inputed date is in the past")
        return v

class BookingCreate(BaseModel):
    user_id: int
    event_id: int



