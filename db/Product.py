from sqlalchemy import Column, Integer, String
from db.ConectionDB import Base, engine


class Product (Base):
    __tablename__ = "PRODUCT"

    id_product = Column(Integer, primary_key=True,
                        unique=True, autoincrement=True)
    name_product = Column(String)
    description = Column(String)
    reference = Column(String)
    price = Column(Integer)


# Con esta línea se hace el proceso de creación de la tabla.
Base.metadata.create_all(bind=engine)
