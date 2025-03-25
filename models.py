import datetime
from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Group(Base):
    __tablename__ = 'groups'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    students: Mapped[list['Student']] = relationship(back_populates='group', cascade="all, delete")

class Student(Base):
    __tablename__ = 'students'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    group_id: Mapped[int] = mapped_column(ForeignKey('groups.id', ondelete='CASCADE'))
    group: Mapped['Group'] = relationship(back_populates='students')
    grades: Mapped[list['Grade']] = relationship(back_populates='student', cascade="all, delete")

    def __repr__(self):
        return f"Student(id={self.id}, name={self.name}, group_id={self.group_id})"

class Teacher(Base):
    __tablename__ = 'teachers'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    subjects: Mapped[list['Subject']] = relationship(back_populates='teacher', cascade="all, delete")

class Subject(Base):
    __tablename__ = 'subjects'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    teacher_id: Mapped[int] = mapped_column(ForeignKey('teachers.id', ondelete='CASCADE'))
    teacher: Mapped['Teacher'] = relationship(back_populates='subjects')
    grades: Mapped[list['Grade']] = relationship(back_populates='subject', cascade="all, delete")

class Grade(Base):
    __tablename__ = 'grades'
    id: Mapped[int] = mapped_column(primary_key=True)
    student_id: Mapped[int] = mapped_column(ForeignKey('students.id', ondelete='CASCADE'))
    subject_id: Mapped[int] = mapped_column(ForeignKey('subjects.id', ondelete='CASCADE'))
    grade: Mapped[int] = mapped_column(nullable=False)
    date_received: Mapped[datetime.date] = mapped_column(nullable=False)

    student: Mapped['Student'] = relationship(back_populates='grades')
    subject: Mapped['Subject'] = relationship(back_populates='grades')

    __table_args__ = (CheckConstraint('grade BETWEEN 1 AND 12', name='valid_grade'),)

    def __repr__(self):
        return f"Grade(id={self.id}, student_id={self.student_id}, subject_id={self.subject_id}, grade={self.grade}, date_received={self.date_received})"
