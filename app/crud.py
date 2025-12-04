from sqlalchemy.orm import Session
from passlib.context import CryptContext
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