import models 
from sqlalchemy.orm import Session
from db.User import User


def  get_user (session_user: Session, username):
    return session_user.query(User).filter(User.username == username).first()