import random
from faker import Faker
from connect import session  # Використовуємо існуючу сесію
from models import Group, Student, Teacher, Subject, Grade

fake = Faker()


def seed_database():
    # Створення груп
    groups = [Group(name=f"Group {i + 1}") for i in range(3)]
    session.add_all(groups)
    session.commit()

    # Створення викладачів
    teachers = [Teacher(name=fake.name()) for _ in range(random.randint(3, 5))]
    session.add_all(teachers)
    session.commit()

    # Створення предметів
    subjects = [Subject(name=fake.word().capitalize(), teacher=random.choice(teachers)) for _ in
                range(random.randint(5, 8))]
    session.add_all(subjects)
    session.commit()

    # Створення студентів
    students = [Student(name=fake.name(), group=random.choice(groups)) for _ in range(random.randint(30, 50))]
    session.add_all(students)
    session.commit()

    # Створення оцінок для кожного студента
    for student in students:
        for subject in subjects:
            grades = [
                Grade(
                    student=student,
                    subject=subject,
                    grade=random.randint(1, 10),
                    date_received=fake.date_between(start_date="-1y", end_date="today")
                )
                for _ in range(random.randint(10, 20))
            ]
            session.add_all(grades)
    session.commit()


if __name__ == "__main__":
    seed_database()
    print("Database successfully seeded!")
