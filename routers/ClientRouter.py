from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from db.Client import Client
from db.ConectionDB import get_db
from models.ClientModels import ClientIn, ClientOut
from repository import ClientRepository


router = APIRouter()


@router.get("/client/{identification_document}",response_model=ClientOut)
async def auth_client(identification_document: str, user_session: Session = Depends(get_db)):
    client = ClientRepository.get_client(user_session, identification_document)
    print()
    if client == None:
        raise HTTPException(status_code=404,
                            detail="El cliente no existe")
    return client

