import argparse
from connect import session
from models import Teacher, Student, Group, Subject, Grade


def create_teacher(name):
    teacher = Teacher(name=name)
    session.add(teacher)
    session.commit()
    print(f"Teacher '{name}' created with ID {teacher.id}")


def list_teachers():
    teachers = session.query(Teacher).all()
    for teacher in teachers:
        print(f"ID: {teacher.id}, Name: {teacher.name}")


def update_teacher(teacher_id, name):
    teacher = session.query(Teacher).get(teacher_id)
    if teacher:
        teacher.name = name
        session.commit()
        print(f"Teacher ID {teacher_id} updated to '{name}'")
    else:
        print(f"Teacher with ID {teacher_id} not found")


def remove_teacher(teacher_id):
    teacher = session.query(Teacher).get(teacher_id)
    if teacher:
        session.delete(teacher)
        session.commit()
        print(f"Teacher ID {teacher_id} removed")
    else:
        print(f"Teacher with ID {teacher_id} not found")


def main():
    parser = argparse.ArgumentParser(description="CLI for database CRUD operations")
    parser.add_argument("-a", "--action", choices=["create", "list", "update", "remove"], required=True,
                        help="Action to perform")
    parser.add_argument("-m", "--model", choices=["Teacher", "Student", "Group", "Subject", "Grade"], required=True,
                        help="Model to operate on")
    parser.add_argument("-id", type=int, help="ID of the record (for update/remove)")
    parser.add_argument("-n", "--name", type=str, help="Name (for create/update)")
    args = parser.parse_args()

    if args.model == "Teacher":
        if args.action == "create":
            if args.name:
                create_teacher(args.name)
            else:
                print("Error: --name is required for create action")
        elif args.action == "list":
            list_teachers()
        elif args.action == "update":
            if args.id and args.name:
                update_teacher(args.id, args.name)
            else:
                print("Error: --id and --name are required for update action")
        elif args.action == "remove":
            if args.id:
                remove_teacher(args.id)
            else:
                print("Error: --id is required for remove action")
    else:
        print("Model not implemented yet")


if __name__ == "__main__":
    main()
