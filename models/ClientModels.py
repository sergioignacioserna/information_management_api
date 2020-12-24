from pydantic import BaseModel


class ClientIn(BaseModel):
    identification_document: str


class ClientOut(BaseModel):
    id_client: str
    email: str
    name: str
    last_name: str
    telefhone: int
    email: str
    direction: str

    class Config:
        orm_mode = True
