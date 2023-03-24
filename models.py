from typing import Optional,List
from pydantic import BaseModel

from sqlalchemy import Column,Integer,String,ForeignKey,TIMESTAMP,Date,Time,Boolean
from databse import Base,engine
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer , primary_key=True,index=True)
    username = Column(String, unique=True)
    fullname = Column(String)
    email = Column(String , unique=True,index=True)
    gender = Column(String)
    age = Column(Integer)
    hashed_password = Column(String)
    
    canvas = relationship('Canvas', back_populates="users")
    address = relationship('Address', back_populates="users")
    images = relationship('SavedImages', back_populates="users")
    
    
class Canvas(Base):
    __tablename__ = "canvas"
    canvas_id = Column(Integer , primary_key=True,index=True)
    color = Column(String)
    brush = Column(String)
    eraser = Column(String)
    triangle = Column(String)
    rectangle = Column(String)
    circle = Column(String)
    user_id = Column(Integer , ForeignKey('users.user_id'),index=True)
    users = relationship('User', back_populates="canvas")

class Address(Base):
    __tablename__ = "address"
    id = Column(Integer , primary_key=True,index=True)
    address1 = Column(String)
    address2 = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    postalcode = Column(String)
    user_id = Column(Integer , ForeignKey('users.user_id'),index=True)
    users = relationship('User',back_populates="address")

    

class LoginHistory(Base):
    __tablename__ = "login_history"
    user_id= Column(Integer , primary_key=True,index=True)
    created_time = Column(TIMESTAMP,primary_key=True,index=True)
    login_state =Column(Boolean)
   

   
class SavedImages(Base):
    __tablename__ = "saved_images"
    image_id = Column(String , primary_key=True,index=True)
    image_path = Column(String)
    insert_date = Column(Date)
    insert_time = Column(Time) 
    user_id = Column(Integer , ForeignKey('users.user_id'),index=True)
    users = relationship('User',back_populates="images")

    
    
# Base.metadata.create_all(bind=engine)
    
# app=FASTAPI() 

# relationship