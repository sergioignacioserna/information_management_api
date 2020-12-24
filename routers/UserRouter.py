from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from db.User import User
from db.ConectionDB import get_db
from models.UserModels import UserIn, UserOut
from repository import UserRepository


router = APIRouter()
@router.post("/user/auth/")
async def auth_user(user_in: UserIn, user_session: Session = Depends(get_db)):
    user=UserRepository.get_user(user_session,user_in.username)
    if user == None:
     raise HTTPException(status_code=404,
        detail="El usuario no existe")
    if user.password!= user_in.password:
     raise HTTPException(status_code=403,
         detail="Error de autenticacion")
    return {"Autenticado": True}
