from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Creando Motor y Conexion con la Base de Datos
#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/G3M3E10"
SQLALCHEMY_DATABASE_URL = "postgres://lixrdwmnbqhpup:05942cce3e25d8464645552e5cc042dafdbeb810c0422ca60d34603c412170a4@ec2-3-211-48-92.compute-1.amazonaws.com:5432/d4jc6kqk0i4onu"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Creacion de la Sesion
SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Creando Base para la creacion de los modelos
Base = declarative_base()
Base.metadata.schema = "gestion_informacion"
