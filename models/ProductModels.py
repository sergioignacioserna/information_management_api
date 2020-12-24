from pydantic import BaseModel

class ProductIn(BaseModel):
    reference: str


class ProductOut(BaseModel):
    name_product: str
    description: str
    price: int
    reference: str

    class Config:
        orm_mode = True
