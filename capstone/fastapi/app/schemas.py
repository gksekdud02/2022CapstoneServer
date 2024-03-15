from xmlrpc.client import DateTime
from pydantic import BaseModel, EmailStr
from typing import List, Optional

class User(BaseModel):
    nickname: str
    login_id: str
    login_pw: str
    name: str
    email: EmailStr
    phone: str

    class Config:
        orm_mode = True

class statRoom(BaseModel):
    id:int
    created_at: str
    temp: float
    humidity: int
    finedust: int
    ledcolor: str

class Room(BaseModel):
    temp: float
    humidity : int
    finedust: int
    ledcolor: str

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    login_id: str
    login_pw: str
    
    class Config:
        orm_mode = True


class Token(BaseModel):
    Authorizaion: str= None
    
    class Config:
        orm_mode = True

class UserToken(BaseModel):
    id: int  
    nickname: str
    login_id: str
    #login_pw: str
    name: str
    email: EmailStr
    phone: str

    class Config:
        orm_mode = True
