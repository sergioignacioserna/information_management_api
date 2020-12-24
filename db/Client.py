from sqlalchemy import Column, Integer, String
from db.ConectionDB import Base, engine

class Client (Base):
    __tablename__ = "CLIENT"

    id_client = Column(Integer, primary_key=True,
                       unique=True, autoincrement=True)
    identification_document = Column(String, unique=True)
    name = Column(String)
    last_name = Column(String)
    telefhone = Column(String)
    email = Column(String)
    direction = Column(String)


# Con esta línea se hace el proceso de creación de la tabla.
Base.metadata.create_all(bind=engine)
