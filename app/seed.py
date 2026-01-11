from .database import sessionlocal , engine
from . import models

db = sessionlocal()
db.query(models.Booking).delete()
db.query(models.Event).delete()
db.query(models.user).delete()
db.query(models.Venue).delete()
db.commit()
print("database cleared")

db_venue = models.Venue( id = 1,name = "testname" , location = "testlocation" ,  capacity = 1000)
db.add(db_venue)
db.commit()
db.refresh(db_venue)
if(db_venue != None):
    print("venue created")

db_event = models.Event(id=1 ,name = "test.event.name" , date = "2023-12-12", venue_id = 1)
db.add(db_event)
db.commit()
db.refresh(db_event)
if(db_event != None):
    print("event created")

for i in range(1, 10001):
    db_user = models.user(id = i, email=f"test.email:{i}" , username = f"test.username:{i}" , hashed_password = "hashedpassasdafaefa") 
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
if(db_user != None):
    print("users created")
