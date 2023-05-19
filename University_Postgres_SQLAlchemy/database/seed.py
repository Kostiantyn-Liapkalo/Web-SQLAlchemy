from datetime import datetime
from random import randint, choice

from faker import Faker

from db_connection import session
from models import Professor, Student, Group, Subject, Mark

fake_data = Faker()

NUMBER_OF_PROFESSORS = 3
NUMBER_OF_STUDENTS = 30
NUMBER_OF_GROUPS = 3
NUMBER_OF_SUBJECTS = 5
NUMBER_OF_MARKS = 150

date_start = datetime.strptime("2022-01-01", "%Y-%m-%d")
date_end = datetime.strptime("2022-12-31", "%Y-%m-%d")
random_date = [
    fake_data.date_between_dates(date_start=date_start, date_end=date_end)
    for _ in range(10)
]


def connections():
    # Data from queries
    students = session.query(Student).all()
    students_ids = session.query(Student.id).all()
    subjects = session.query(Subject).all()
    subjects_ids = session.query(Subject.id).all()
    groups_ids = session.query(Group.id).all()
    professors_ids = session.query(Professor.id).all()
    marks = session.query(Mark).all()

    # Connect students-group_id
    for student in students:
        student.group_id = choice([g_id[0] for g_id in groups_ids])
    session.commit()

    # Connect marks-student_id-professor_id
    for mark in marks:
        mark.student_id = choice([student_id[0] for student_id in students_ids])
        mark.professor_id = choice([professor_id[0] for professor_id in professors_ids])
        mark.subject_id = choice([subject_id[0] for subject_id in subjects_ids])
    session.commit()

    # Connect subject-professor_id
    for subject in subjects:
        subject.professor_id = choice([professor_id[0] for professor_id in professors_ids])
    session.commit()


def generate_fake_data():

    for _ in range(NUMBER_OF_PROFESSORS):
        fake_professor = Professor(name=fake_data.name(), email=fake_data.email())
        session.add(fake_professor)

    session.commit()

    for _ in range(NUMBER_OF_STUDENTS):
        fake_student = Student(name=fake_data.name())
        session.add(fake_student)

    session.commit()

    for _ in range(NUMBER_OF_GROUPS):
        fake_group = Group(name=fake_data.job())
        session.add(fake_group)

    session.commit()

    for _ in range(NUMBER_OF_SUBJECTS):
        fake_subject = Subject(name=fake_data.job())
        session.add(fake_subject)

    session.commit()

    for _ in range(NUMBER_OF_MARKS):
        fake_mark = Mark(mark=randint(1, 100), date=choice(random_date))
        session.add(fake_mark)

    session.commit()


if __name__ == '__main__':
    generate_fake_data()
    connections()

    #p = session.query(Professor).all()
    #s = session.query(Student).all()
    #ss= session.query(Subject).all()
    #m = session.query(Mark).all()
    #g = session.query(Group).all()

    #for mark in m:
    #    session.delete(mark)
    #for d in p:
    #    session.delete(d)
    #for a in s:
    #    session.delete(a)
    #for v in ss:
    #    session.delete(v)
    #for u in g:
    #    session.delete(u)

    #session.commit()