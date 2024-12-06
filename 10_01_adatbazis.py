import datetime
from peewee import SqliteDatabase, Model, CharField, DateField, IntegerField, ForeignKeyField

db = SqliteDatabase("neptun100.db")

class Student(Model):
    name = CharField(max_length=255)
    birthdate = DateField()

    class Meta:
        database = db

class Subject(Model):
    name = CharField(max_length=255)

    class Meta:
        database = db

class Mark(Model):
    student = ForeignKeyField(Student, backref="marks")
    subject = ForeignKeyField(Subject, backref="marks")
    mark = IntegerField()

    class Meta:
        database = db

def init_db():
    db.create_tables([Student, Subject, Mark])

def fill_db():
    gipsz_jakab = Student(name="Gipsz Jakab", birthdate=datetime.date(1990, 1, 1))
    gipsz_jakab.save()
    matek = Subject(name="Matek")
    matek.save()
    fizika = Subject(name="Fizika")
    fizika.save()
    magyar = Subject(name="Magyar")
    magyar.save()

def give_mark_demo():
    gipsz_jakab = Student.get(name="Gipsz Jakab")
    matek = Subject.get(name="Matek")
    Mark(student=gipsz_jakab, subject=matek, mark=5).save()

def list_students():
    for student in Student.select():
        print(student.name)
        for mark in student.marks:
            print(f"    {mark.subject.name}: {mark.mark}")

if __name__ == "__main__":
    init_db()
    fill_db()
    give_mark_demo()
    list_students()
