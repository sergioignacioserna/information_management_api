import models
from sqlalchemy.orm import Session
from db.Client import Client


def get_client(sesion_client: Session,  identification_document):
    return sesion_client.query(Client).filter(Client.identification_document == identification_document).first()
