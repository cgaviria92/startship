from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session


# URL de la base de datos
DATABASE_URL = "sqlite:///./test.db"

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Declarar una clase base para los modelos de SQLAlchemy
Base = declarative_base()

# Definir una función para obtener una sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

