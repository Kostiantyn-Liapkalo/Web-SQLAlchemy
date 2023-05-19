from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from db_connection import Base


class Professor(Base):

    __tablename__ = 'professors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(75), nullable=True)
    email = Column(String(75), unique=True)
    subjects = relationship('Subject', back_populates='professor')
    marks = relationship('Mark', back_populates='professor')


class Student(Base):

    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(75), nullable=True)
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship('Group', back_populates='students')
    marks = relationship('Mark', back_populates='student')


class Group(Base):

    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(75), nullable=True)
    students = relationship('Student', back_populates='group')


class Subject(Base):

    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(75), nullable=True)
    professor_id = Column(Integer, ForeignKey('professors.id'))
    professor = relationship('Professor', back_populates='subjects')
    mark = relationship('Mark', back_populates='subject')


class Mark(Base):

    __tablename__ = 'marks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    mark = Column(Integer)
    date = Column(Date)
    student_id = Column(Integer, ForeignKey('students.id'))
    professor_id = Column(Integer, ForeignKey('professors.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    professor = relationship('Professor', back_populates='marks')
    student = relationship('Student', back_populates='marks')
    subject = relationship('Subject', back_populates='mark')
