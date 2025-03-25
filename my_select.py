from sqlalchemy.orm import joinedload
from sqlalchemy.sql import func
from connect import session
from models import Student, Grade, Subject, Teacher, Group

def select_1():
    return session.query(Student.name, func.avg(Grade.grade).label("avg_grade"))\
        .join(Grade)\
        .group_by(Student.id)\
        .order_by(func.avg(Grade.grade).desc())\
        .limit(5)\
        .all()

def select_2(subject_id):
    return session.query(Student.name, func.avg(Grade.grade).label("avg_grade"))\
        .join(Grade)\
        .filter(Grade.subject_id == subject_id)\
        .group_by(Student.id)\
        .order_by(func.avg(Grade.grade).desc())\
        .first()

def select_3(subject_id):
    result = (
        session.query(
            Group.name,
            func.avg(Grade.grade).label("avg_grade")
        )
        .join(Student, Student.group_id == Group.id)
        .join(Grade, Grade.student_id == Student.id)
        .filter(Grade.subject_id == subject_id)
        .group_by(Group.name)
        .all()
    )
    return result

def select_4():
    return session.query(func.avg(Grade.grade).label("avg_grade"))\
        .scalar()

def select_5(teacher_id):
    return session.query(Subject.name)\
        .filter(Subject.teacher_id == teacher_id)\
        .all()

def select_6(group_id):
    return session.query(Student.name)\
        .filter(Student.group_id == group_id)\
        .all()

def select_7(group_id, subject_id):
    return session.query(Student.name, Grade.grade)\
        .join(Grade)\
        .filter(Student.group_id == group_id, Grade.subject_id == subject_id)\
        .all()

def select_8(teacher_id):
    return session.query(func.avg(Grade.grade).label("avg_grade"))\
        .join(Subject).filter(Subject.teacher_id == teacher_id)\
        .scalar()

def select_9(student_id):
    return session.query(Subject.name)\
        .join(Grade).filter(Grade.student_id == student_id)\
        .distinct()\
        .all()

def select_10(student_id, teacher_id):
    return session.query(Subject.name)\
        .join(Grade).filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id)\
        .distinct()\
        .all()

if __name__ == "__main__":
    print("5 студентів із найбільшим середнім балом:", select_1())
    print("Студент із найвищим середнім балом з предмета 1:", select_2(1))
    print("Середній бал у групах з предмета 1:", select_3(1))
    print("Середній бал на потоці:", select_4())
    print("Курси викладача 1:", select_5(1))
    print("Список студентів у групі 1:", select_6(1))
    print("Оцінки студентів у групі 1 з предмета 1:", select_7(1, 1))
    print("Середній бал, який ставить викладач 1:", select_8(1))
    print("Курси, які відвідує студент 1:", select_9(1))
    print("Курси, які студенту 1 читає викладач 1:", select_10(1, 1))
