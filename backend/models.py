from typing import List
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    
class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    students = relationship("Student", back_populates="promotion")

class StudentSchema(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True

class PromotionSchema(BaseModel):
    name: str
    students: List[StudentSchema] = []

    class Config:
        orm_mode = True