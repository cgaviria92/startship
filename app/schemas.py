from typing import List, Optional
from fastapi.datastructures import Default

from pydantic import BaseModel, Field, EmailStr,validator
from bson import ObjectId
from sqlalchemy.sql.sqltypes import Integer
from schematics.models import Model
from schematics.types import StringType, EmailType



# class ItemBase(BaseModel):

#     title: str

#     description: Optional[str] = None




# class ItemCreate(ItemBase):

#     pass



# class Item(ItemBase):
#     id: int
#     owner_id: int

#     class Config:
#         orm_mode = True



# class UserBase(BaseModel):
#     username: str
#     email: str




# class UserCreate(UserBase):

#     password: str


################################


class User(Model):
    user_id = ObjectId()
    email = EmailType(required=True)
    username = StringType(required=True)
    password = StringType(required=True)
    #money = Integer(Default=100)
newuser = User()
def create_user(email, username, password):
    newuser.user_id = ObjectId()
    newuser.email = email
    newuser.username = username
    newuser.password = password
    
    return dict(newuser)

def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "money": item["money"],
        "exp": item["exp"],
        "hp_current": item["hp_current"],
        "ship_use": item["ship_use"],
        "ship_active": item["ship_active"],
        "bonus_repair_robot": item["bonus_repair_robot"],
        "bonus_enhancer_speed": item["bonus_enhancer_speed"],
        "bonus_enhancer_shield": item["bonus_enhancer_shield"],
        "update_hp": item["update_hp"],
        "update_speed": item["update_speed"],
        "update_damage": item["update_damage"],
        "update_critical": item["update_critical"]

    }


class User_update(BaseModel):
    location_x:Optional[int]
    location_y:Optional[int]
    location_map:Optional[int]
    money:Optional[int]
    exp:Optional[int]
    hp_current:Optional[int]
    ship_use:Optional[int]
    ship_active:Optional[int]
    bonus_repair_robot:Optional[int]
    bonus_enhancer_critical:Optional[int]
    bonus_enhancer_speed:Optional[int]
    bonus_enhancer_shield:Optional[int]
    update_hp:Optional[int]
    update_speed:Optional[int]
    update_damage:Optional[int]
    update_critical:Optional[int]


    # @validator('username')
    # def name_must_contain_space(cls, v):
    #     if ' ' not in v:
    #         raise ValueError('must contain a space')
    #     return v.title()

 
# baz = User_update(bar=None)
# assert baz.dict(exclude_unset=True) == {"bar": None}

class User_update2(BaseModel):
    
    location_x: Optional[int]
    location_y: Optional[int]
    location_map: Optional[int]
    money: Optional[int]
    exp: Optional[int]
    hp_current: Optional[int]
    ship_use: Optional[int]
    ship_active: Optional[int]
    bonus_repair_robot: Optional[int]
    bonus_enhancer_critical: Optional[int]
    bonus_enhancer_speed: Optional[int] 
    bonus_enhancer_shield: Optional[int] 
    update_hp: Optional[int] 
    update_speed: Optional[int] 
    update_damage: Optional[int] 
    update_critical: Optional[int] 
####################

class User_login(BaseModel):
    username:str
    password: str
    

class User_register_post(BaseModel):
    _id = ObjectId()
    username:str
    password: str
    email : str
#############

# class user_all_info_login(BaseModel):
#     id_user: int
#     locations_id= int
#     infousers_id = int
#     infousers_money  = int
#     infousers_exp  = int
#     infousers_hp_current  = int
#     ship_hp_update= int
#     ship_speed= int
#     ship_speed_update = int
#     ship_damage = int
#     ship_damage_update = int
#     ship_critical = int
#     ship_critical_update = int


# class PyObjectId(ObjectId):
#     @classmethod
#     def __get_validators__(cls):
#         yield cls.validate

#     @classmethod
#     def validate(cls, v):
#         if not ObjectId.is_valid(v):
#             raise ValueError("Invalid objectid")
#         return ObjectId(v)

#     @classmethod
#     def __modify_schema__(cls, field_schema):
#         field_schema.update(type="string")

# class UserCreatetModel(BaseModel):
#     id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
#     name: str = Field(...)
#     password: str = Field(...)
#     email: EmailStr = Field(...)
#     is_active : bool = Field(True)
#     experience : int = Field(100)
#     money : int = Field(100)
#     hp_current =  Field(100)
   

#     class Config:
#         allow_population_by_field_name = True
#         arbitrary_types_allowed = True
#         json_encoders = {ObjectId: str}
#         schema_extra = {
#             "example": {
#                 "name": "carlos",
#                 "password":"123456789",
#                 "email": "jdoe@example.com"
#             }
#         }