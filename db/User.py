from sqlalchemy import Column, Integer, String
from db.ConectionDB import Base, engine


class User(Base):
    __tablename__ = 'USERS'

    id_user = Column(Integer, primary_key=True,
                     unique=True, autoincrement=True)
    name = Column(String)
    last_name = Column(String)
    email = Column(String)
    position = Column(String)
    username = Column(String, unique=True)
    password = Column(String)


# Con esta línea se hace el proceso de creación de la tabla.
Base.metadata.create_all(bind=engine)
