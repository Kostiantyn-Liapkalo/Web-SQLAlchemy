from sqlalchemy import func, desc
from sqlalchemy.orm import joinedload


from db_connection import session
from models import Professor, Student, Group, Subject, Mark


def select_1():
    result = session.query(
        Mark.student_id,
        Student.name,
        func.avg(Mark.mark).label('avg_mark')
    ).join(
        Student, Student.id == Mark.student_id
    ).group_by(
        Mark.student_id,
        Student.name
    ).order_by(
        desc('avg_mark')
    ).limit(5).all()

    return result


def select_2():
    result = session.query(
        Mark.student_id,
        Student.name,
        Subject.name,
        func.avg(Mark.mark).label('avg_mark')
    ).join(
        Student, Student.id == Mark.student_id
    ).join(
        Subject, Subject.id == Mark.subject_id
    ).filter(
        Subject.name == 'Make'
    ).group_by(
        Mark.student_id,
        Student.name,
        Subject.name
    ).order_by(
        func.avg(Mark.mark).desc()
    ).limit(1).all()

    return result


def select_3():
    subquery = (
        session.query(Student.id)
        .filter(Student.group_id.between(7, 9))
        .subquery()
    )

    stmt = (
        session.query(Group.id, Group.name, func.avg(Mark.mark).label('avg_mark'))
        .join(Student, Student.group_id == Group.id)
        .join(Mark, Mark.student_id == Student.id)
        .join(Subject, Mark.subject_id == Subject.id)
        .filter(Student.id.in_(subquery))
        .filter(Subject.name == 'Make')
        .group_by(Group.id, Group.name)
        .order_by(func.avg(Mark.mark).desc())
    )

    result = stmt.all()
    return result


def select_4():
    result = session.query(func.avg(Mark.mark)).scalar()

    return result


def select_5():
    result = session.query(Subject.name, Professor.id, Professor.name).join(Professor).filter(Subject.professor_id == 7).all()

    return result


def select_6():
    result = session.query(Student.id, Student.name).filter(Student.group_id == 7).all()

    return result


def select_7():
    result = session.query(Student.id, Student.name, Mark.mark, Subject.name).join(Mark, Student.id == Mark.student_id)\
        .join(Subject, Subject.id == Mark.subject_id)\
        .filter(Student.group_id == 8, Subject.name == 'Make').all()

    return result


def select_8():
    result = (
        session.query(
            func.avg(Mark.mark).label('avg_mark'),
            Professor.name,
            Professor.id
        )
        .join(Subject, Subject.professor_id == Professor.id)
        .join(Mark, Mark.subject_id == Subject.id)
        .filter(Professor.id == 8)
        .group_by(Professor.id, Professor.name)
        .all())

    return result


def select_9():
    result = (session
    .query(Mark.student_id, Subject.name)
    .join(Mark, Mark.subject_id == Subject.id)
    .filter(Mark.student_id == 61)
    .all())

    return result


def select_10():
    result = session.query(Subject.id, Subject.name)\
        .join(Mark, Subject.id == Mark.subject_id)\
        .filter(Mark.student_id == 65, Subject.professor_id == 8)\
        .all()

    return result


if __name__ == '__main__':
    print(select_10())
