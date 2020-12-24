from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from db.Product import Product
from db.ConectionDB import get_db
from models.ProductModels import ProductIn, ProductOut
from repository import ProductRepository


router = APIRouter()
@router.get("/product/{reference}",response_model=ProductOut)
async def auth_product(reference: str, product_session: Session = Depends(get_db)):
    product=ProductRepository.get_product(product_session,reference)
    if product == None:
     raise HTTPException(status_code=404,
        detail="El producto no existe")
    return product


