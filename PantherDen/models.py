from app import Base
from sqlalchemy import Column, Integer, String, Date


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    firstname = Column(String(50))
    lastname = Column(String(50))
    homeroomid = Column(Integer)


class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True)
    firstname = Column(String(50))
    lastname = Column(String(50))
    roomid = Column(Integer)


class Schedule(Base):
    __tablename__ = "schedules"

    roomid = Column(Integer)
    studentid = Column(Integer)
    oldroomid = Column(Integer)
    date = Column(Date)
