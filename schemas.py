from typing import List, Optional


from pydantic import BaseModel




class ItemBase(BaseModel):

    title: str

    description: Optional[str] = None




class ItemCreate(ItemBase):

    pass



class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True



class UserBase(BaseModel):
    username: str
    email: str




class UserCreate(UserBase):

    password: str



class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True

class User_login(BaseModel):
    username:str
    password: str

class user_all_info_login(BaseModel):
    id_user: int
    locations_id= int
    infousers_id = int
    infousers_money  = int
    infousers_exp  = int
    infousers_hp_current  = int
    ship_hp_update= int
    ship_speed= int
    ship_speed_update = int
    ship_damage = int
    ship_damage_update = int
    ship_critical = int
    ship_critical_update = int