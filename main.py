from fastapi import FastAPI, Depends
# from models import User
# from config.db import conn
from databse import Base,engine,sessionlocal
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from models import Canvas
import models


Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    try:
        db = sessionlocal()
        yield db
    finally:
        db.close()
        
class CanvasSchema(BaseModel):
    color: str
    brush: str
    eraser: str
    triangle: str
    rectangle: str
    circle: str
    user_id: int
   
@app.get("/")
async def helloworld():
    return {"message": "Hello World"}


@app.get("/all-users")
async def get_all_users(db: Session = Depends(get_db)):
    all_users = db.query(models.User).all()
    return all_users


@app.post("/canvas")
async def save_canvas_details(canvas : CanvasSchema,db:Session=Depends(get_db)):
    u=Canvas(color=canvas.color,brush=canvas.brush,eraser=canvas.eraser,triangle=canvas.triangle,rectangle=canvas.rectangle,circle=canvas.circle,user_id=canvas.user_id)
    db.add(u)
    db.commit()
    return(u)

