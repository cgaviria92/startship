from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#pruebas
#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Micro2020@127.0.0.1:5432/startship"
#pruduccion
SQLALCHEMY_DATABASE_URL = "postgres://ussgtiyqthumim:1e20dfdc0dd51fb8566a09b4b56af020abb80638813fdcb43485d94bc3ed40b6@ec2-34-234-12-149.compute-1.amazonaws.com:5432/d9qpd89l69b1is"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
