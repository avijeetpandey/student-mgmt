from sqlalchemy import Column, Integer, String
from app.database import Base

class Student(Base):
    __tablename__ = 'student_record'

    id =Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    age = Column(Integer, nullable=False)
