import models
from sqlalchemy.orm import Session
from db.Product import Product


def get_product(db_product: Session, reference):
    return db_product.query(Product).filter(Product.reference == reference).first()
