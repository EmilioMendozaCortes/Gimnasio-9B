from sqlalchemy.orm import Session
from models import users

def get_users(db:Session, skip: int=0, limit:int=10):
    users = db.query(users).offset(skip.limit).all()