from sqlalchemy.orm import Session

#from . import models, schemas
from models import User,Item,locations,infousers,ship,bonus
from schemas import UserCreate,ItemCreate

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def get_info_all_users(db: Session, user_id: int):
    locations_user=db.query(locations).filter(User.id == user_id).first()
    infousers_user=db.query(infousers).filter(User.id == user_id).first()
    ship_user=db.query(ship).filter(User.id == user_id).first()
    bonus_user=db.query(bonus).filter(User.id == user_id).first()
    return ({"user_id": user_id,
    "locations_id": locations_user.id,
    "locations_x": locations_user.x,
    "locations_y": locations_user.y,
    "locations_map": locations_user.map,
    "infousers_id": infousers_user.id,
    "infousers_money": infousers_user.money,
    "infousers_exp": infousers_user.exp,
    "infousers_hp_current": infousers_user.hp_current,
    "ship_id": ship_user.id,
    "ship_hp": ship_user.hp,
    "ship_update": ship_user.hp_update,
    "ship_speed": ship_user.id,
    "ship_speed_update": ship_user.speed_update,
    "ship_damage": ship_user.damage,
    "ship_damage": ship_user.damage_update,
    "ship_damage": ship_user.critical,
    "ship_damage": ship_user.critical_update,
    "bonus_id": bonus_user.id
    })

def create_user_db(db: Session, user: UserCreate):
    db_user = User(email=user.email, hashed_password=user.password, username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db_locations = locations(user_id=db_user.id)
    db.add(db_locations)
    db_infousers = infousers(user_id=db_user.id)
    db.add(db_infousers)
    db_ship = ship(user_id=db_user.id)
    db.add(db_ship)
    db_bonus = bonus(user_id=db_user.id)
    db.add(db_bonus)
    db.commit()
    #db.refresh(db_locations)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: ItemCreate, user_id: int):
    db_item = Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item