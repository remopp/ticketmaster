from sqlalchemy import Column,Integer,String,Boolean
from .database import base


class user(base):
    __tablename__= "users"
    id = Column(Integer, primary_key=True, index = True)
    email = Column(String , unique=True, index= True)
    hashed_password = Column(String)
    is_active = Column(Boolean , default=True)