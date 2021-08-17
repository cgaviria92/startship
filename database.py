from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#pruebas
#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Micro2020@127.0.0.1:5432/startship"
#pruduccion
SQLALCHEMY_DATABASE_URL = "postgres://cetrwijkygzrya:462f033529889114d5f42adb57ea0eea8e755b755b808fc9e87e48848c3e631d@ec2-52-86-25-51.compute-1.amazonaws.com:5432/df2opdlv8197f7"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
