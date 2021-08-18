from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    #email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    username= Column(String(20),unique=True,index=True)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")



class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")

class locations(Base):
    __tablename__= 'locations'
    id= Column(Integer, primary_key=True)
    x= Column(Integer ,default=1)
    y= Column(Integer, default=1)
    map= Column(Integer, default=1)
    user_id = Column(Integer, ForeignKey('users.id'),unique=True,index=True)

class infousers(Base):
    __tablename__= 'infousers'
    id= Column(Integer, primary_key=True)
    money= Column(Integer, default=1000)
    exp= Column(Integer, default=0)
    #vida actual
    hp_current = Column(Integer, default=100)
    user_id = Column(Integer, ForeignKey('users.id'),unique=True,index=True)

class ship_update(Base):
    __tablename__= 'ship_update'
    id= Column(Integer, primary_key=True)
    # se suma estos dos para la vida maxima
    #hp= Column(Integer,default=1000)
    #vida extra que puede comprar el usuario
    hp_update= Column(Integer,default=0)
    #speed= Column(Integer,default=100)
    speed_update = Column(Integer,default=0)
    #damage = Column(Integer,default=100)
    damage_update = Column(Integer,default=0)
    #critical = Column(Integer,default=0)
    critical_update = Column(Integer,default=0)
    user_id = Column(Integer, ForeignKey('users.id'),unique=True,index=True)

class ship(Base):
    __tablename__= 'ship'
    id= Column(Integer, primary_key=True)
    useship= Column(Integer,default=1)
    is_active = Column(Boolean, default=True)
    
    user_id = Column(Integer, ForeignKey('users.id'),unique=True,index=True)

class bonus(Base):
    __tablename__= 'bonus'
    id= Column(Integer, primary_key=True)
    repair_robot= Column(Integer,default=50)
    enhancer_critical= Column(Integer,default=0)
    enhancer_speed= Column(Integer,default=0)
    enhancer_escudo = Column(Integer,default=0)
    user_id = Column(Integer, ForeignKey('users.id'),unique=True,index=True)

   