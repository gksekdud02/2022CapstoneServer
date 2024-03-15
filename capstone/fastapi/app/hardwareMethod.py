from fastapi import APIRouter
from requests import Session
from fastapi.params import Depends
from sqlalchemy import desc
from db import get_db

import models, schemas

router = APIRouter(prefix="/hardwareMethod",tags=["hardwareMethod"])

@router.get("/test",status_code=200)
async def test():
    return {"message":"testOK"}


#방 정보 생성 - 하드웨어
@router.post("/addRoomInfo/{room_name}/{temp}/{humidity}/{finedust}/{ledcolor}",status_code=200)
def add_room(room_name:str, temp:float, humidity:int, finedust:int,ledcolor:str, db:Session = Depends(get_db)):
    db_room_id = db.query(models.RoomList.id).filter_by(room_name=room_name)
    new_roomInfo = models.Room_Management.create(db, auto_commit=True, 
                                    room_id = db_room_id,
                                    temp = temp,
                                    humidity= humidity,
                                    finedust= finedust,
                                    ledcolor= ledcolor)
    db.add(new_roomInfo)
    db.commit()


    return {"message":"success"}