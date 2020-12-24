from pydantic import BaseModel

class UserIn(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id_user: str
    email: str
    class Config:
        orm_mode = True