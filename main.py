import argparse
from models import Teacher, Student, Group, Subject, Grade
from connect import session
from sqlalchemy.exc import IntegrityError


def create_teacher(name):
    try:
        teacher = Teacher(name=name)
        session.add(teacher)
        session.commit()
        print(f"Teacher {name} created successfully!")
    except IntegrityError:
        print(f"Error: Teacher {name} already exists.")
        session.rollback()


def create_student(name, group_id):
    try:
        student = Student(name=name, group_id=group_id)
        session.add(student)
        session.commit()
        print(f"Student {name} created successfully!")
    except IntegrityError:
        print(f"Error: Student {name} already exists.")
        session.rollback()


def create_group(name):
    try:
        group = Group(name=name)
        session.add(group)
        session.commit()
        print(f"Group {name} created successfully!")
    except IntegrityError:
        print(f"Error: Group {name} already exists.")
        session.rollback()


def create_subject(name, teacher_id):
    try:
        subject = Subject(name=name, teacher_id=teacher_id)
        session.add(subject)
        session.commit()
        print(f"Subject {name} created successfully!")
    except IntegrityError:
        print(f"Error: Subject {name} already exists.")
        session.rollback()


def create_grade(student_id, subject_id, grade, date_received):
    try:
        grade_entry = Grade(student_id=student_id, subject_id=subject_id, grade=grade, date_received=date_received)
        session.add(grade_entry)
        session.commit()
        print(f"Grade for student {student_id} in subject {subject_id} added successfully!")
    except IntegrityError:
        print("Error: Unable to add grade.")
        session.rollback()


def list_teachers():
    teachers = session.query(Teacher).all()
    for teacher in teachers:
        print(f"{teacher.id}: {teacher.name}")


def list_students():
    students = session.query(Student).all()
    for student in students:
        print(f"{student.id}: {student.name} (Group {student.group.name})")


def list_groups():
    groups = session.query(Group).all()
    for group in groups:
        print(f"{group.id}: {group.name}")


def list_subjects():
    subjects = session.query(Subject).all()
    for subject in subjects:
        print(f"{subject.id}: {subject.name} (Teacher {subject.teacher.name})")


def list_grades():
    grades = session.query(Grade).all()
    for grade in grades:
        print(f"Student {grade.student.name}, Subject {grade.subject.name}, Grade {grade.grade}")


def update_teacher(teacher_id, name):
    teacher = session.query(Teacher).get(teacher_id)
    if teacher:
        teacher.name = name
        session.commit()
        print(f"Teacher {teacher_id} updated to {name}.")
    else:
        print(f"Teacher with id {teacher_id} not found.")


def update_student(student_id, name, group_id):
    student = session.query(Student).get(student_id)
    if student:
        student.name = name
        student.group_id = group_id
        session.commit()
        print(f"Student {student_id} updated to {name}.")
    else:
        print(f"Student with id {student_id} not found.")


def update_group(group_id, name):
    group = session.query(Group).get(group_id)
    if group:
        group.name = name
        session.commit()
        print(f"Group {group_id} updated to {name}.")
    else:
        print(f"Group with id {group_id} not found.")


def update_subject(subject_id, name, teacher_id):
    subject = session.query(Subject).get(subject_id)
    if subject:
        subject.name = name
        subject.teacher_id = teacher_id
        session.commit()
        print(f"Subject {subject_id} updated to {name}.")
    else:
        print(f"Subject with id {subject_id} not found.")


def update_grade(grade_id, grade, date_received):
    grade_entry = session.query(Grade).get(grade_id)
    if grade_entry:
        grade_entry.grade = grade
        grade_entry.date_received = date_received
        session.commit()
        print(f"Grade {grade_id} updated.")
    else:
        print(f"Grade with id {grade_id} not found.")


def remove_teacher(teacher_id):
    teacher = session.query(Teacher).get(teacher_id)
    if teacher:
        session.delete(teacher)
        session.commit()
        print(f"Teacher {teacher_id} removed.")
    else:
        print(f"Teacher with id {teacher_id} not found.")


def remove_student(student_id):
    student = session.query(Student).get(student_id)
    if student:
        session.delete(student)
        session.commit()
        print(f"Student {student_id} removed.")
    else:
        print(f"Student with id {student_id} not found.")


def remove_group(group_id):
    group = session.query(Group).get(group_id)
    if group:
        session.delete(group)
        session.commit()
        print(f"Group {group_id} removed.")
    else:
        print(f"Group with id {group_id} not found.")


def remove_subject(subject_id):
    subject = session.query(Subject).get(subject_id)
    if subject:
        session.delete(subject)
        session.commit()
        print(f"Subject {subject_id} removed.")
    else:
        print(f"Subject with id {subject_id} not found.")


def remove_grade(grade_id):
    grade_entry = session.query(Grade).get(grade_id)
    if grade_entry:
        session.delete(grade_entry)
        session.commit()
        print(f"Grade {grade_id} removed.")
    else:
        print(f"Grade with id {grade_id} not found.")


def main():
    parser = argparse.ArgumentParser(description="CRUD operations for the database.")
    parser.add_argument("-a", "--action", required=True, choices=["create", "list", "update", "remove"], help="Action to perform")
    parser.add_argument("-m", "--model", required=True, choices=["Teacher", "Student", "Group", "Subject", "Grade"], help="Model to operate on")
    parser.add_argument("-n", "--name", help="Name for create/update")
    parser.add_argument("-id", "--id", type=int, help="ID for update/remove")
    parser.add_argument("-g", "--group_id", type=int, help="Group ID for Student creation/update")
    parser.add_argument("-t", "--teacher_id", type=int, help="Teacher ID for Subject creation/update")
    parser.add_argument("-s", "--subject_id", type=int, help="Subject ID for Grade creation/update")
    parser.add_argument("-gr", "--grade", type=int, help="Grade for Grade creation/update")
    parser.add_argument("-d", "--date_received", type=str, help="Date received for Grade creation/update")

    args = parser.parse_args()

    if args.action == "create":
        if args.model == "Teacher":
            create_teacher(args.name)
        elif args.model == "Student":
            create_student(args.name, args.group_id)
        elif args.model == "Group":
            create_group(args.name)
        elif args.model == "Subject":
            create_subject(args.name, args.teacher_id)
        elif args.model == "Grade":
            create_grade(args.id, args.subject_id, args.grade, args.date_received)
    elif args.action == "list":
        if args.model == "Teacher":
            list_teachers()
        elif args.model == "Student":
            list_students()
        elif args.model == "Group":
            list_groups()
        elif args.model == "Subject":
            list_subjects()
        elif args.model == "Grade":
            list_grades()
    elif args.action == "update":
        if args.model == "Teacher":
            update_teacher(args.id, args.name)
        elif args.model == "Student":
            update_student(args.id, args.name, args.group_id)
        elif args.model == "Group":
            update_group(args.id, args.name)
        elif args.model == "Subject":
            update_subject(args.id, args.name, args.teacher_id)
        elif args.model == "Grade":
            update_grade(args.id, args.grade, args.date_received)
    elif args.action == "remove":
        if args.model == "Teacher":
            remove_teacher(args.id)
        elif args.model == "Student":
            remove_student(args.id)
        elif args.model == "Group":
            remove_group(args.id)
        elif args.model == "Subject":
            remove_subject(args.id)
        elif args.model == "Grade":
            remove_grade(args.id)


if __name__ == "__main__":
    main()
