from enum import unique
from logging import critical
import databases, sqlalchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey,String
from sqlalchemy.orm import backref
from sqlalchemy import UniqueConstraint
from sqlalchemy.sql.dml import Insert
from sqlalchemy.sql.expression import column
from sqlalchemy.sql.schema import PrimaryKeyConstraint
from sqlalchemy.sql.sqltypes import CHAR
## Postgres Database
DATABASE_URL = "postgresql://postgres:Micro2020@127.0.0.1:5432/postgres"
#DATABASE_URL = "postgres://cetrwijkygzrya:462f033529889114d5f42adb57ea0eea8e755b755b808fc9e87e48848c3e631d@ec2-52-86-25-51.compute-1.amazonaws.com:5432/df2opdlv8197f7"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# users = sqlalchemy.Table(
#     "users",
#     metadata,
#     sqlalchemy.Column("id"        , sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column("username"  , sqlalchemy.String),
#     sqlalchemy.Column("password"  , sqlalchemy.String),
#     sqlalchemy.Column("email", sqlalchemy.String),
#     sqlalchemy.Column("last_name" , sqlalchemy.String),
#     #sqlalchemy.Column("gender"    , sqlalchemy.CHAR  ),
#     sqlalchemy.Column("create_at" , sqlalchemy.String),
#     sqlalchemy.Column("status"    , sqlalchemy.CHAR  ),
#     sqlalchemy.Column("money" , sqlalchemy.Integer),

    
# )

# location = sqlalchemy.Table(
#     "location",
#     metadata,
#     sqlalchemy.Column("id"        , sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column("x"  , sqlalchemy.Integer),
#     sqlalchemy.Column("y"  , sqlalchemy.Integer),
#     sqlalchemy.Column("map", sqlalchemy.Integer),
#     #sqlalchemy.Column("user_id" ,sqlalchemy.Integer, ForeignKey('users.id')),  
#     #sqlalchemy.Column("user_id" ,sqlalchemy.Integer, secondary=users)
#     #sqlalchemy.Column("id_users", sqlalchemy.Integer, relationship("Users")),
# )

    
class users(Base):
    __tablename__= 'users'
    id= Column(Integer, primary_key=True)
    username= Column(String(20),unique=True)
    email= Column(String(50),unique=True)
    password= Column(String(50))
    status = Column(CHAR)

class locations(Base):
    __tablename__= 'locations'
    id= Column(Integer, primary_key=True)
    x= Column(Integer)
    y= Column(Integer)
    map= Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'),unique=True)
    
class infousers(Base):
    __tablename__= 'infousers'
    id= Column(Integer, primary_key=True)
    money= Column(Integer)
    exp= Column(Integer)
    #vida actual
    hp_current = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'),unique=True)

class ship(Base):
    __tablename__= 'ship'
    id= Column(Integer, primary_key=True)
    # se suma estos dos para la vida maxima
    hp= Column(Integer)
    #vida extra que puede comprar el usuario
    hp_update= Column(Integer)
    speed= Column(Integer)
    speed_update = Column(Integer)
    damage = Column(Integer)
    damage_update = Column(Integer)
    critical = Column(Integer)
    critical_update = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'),unique=True)

class bonus(Base):
    __tablename__= 'bonus'
    id= Column(Integer, primary_key=True)
    repair_robot= Column(Integer)
    enhancer_critical= Column(Integer)
    enhancer_speed= Column(Integer)
    enhancer_escudo = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'),unique=True)

engine = sqlalchemy.create_engine(
    DATABASE_URL
)
Base.metadata.create_all(engine)