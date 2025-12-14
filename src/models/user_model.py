from sqlalchemy import Column, Integer, String, Date
from src.config.database import Base

class User(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True, index=True, autoincrement=True)
    username=Column(String(50),nullable=True, unique=True, index=True)
    email=Column(String(50),nullable=True,unique=True,index=True)
    password=Column(String(512),nullable=False)
    phone=Column(String(20),nullable=True)
    dob=Column(Date,nullable=True)
    gender=Column(String(10),nullable=True)
    address=Column(String(255),nullable=True)