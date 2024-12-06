import datetime
from peewee import SqliteDatabase, Model, CharField, DateField, IntegerField, ForeignKeyField

db = SqliteDatabase('neptun100.db')

class Student(Model):
    name = CharField(max_length=255)
    birthdate = DateField()
    id = IntegerField(primary_key=True)

    class Meta:
        database = db

class Subject(Model):
    name = CharField(max_length=255)
    id = IntegerField(primary_key=True)

    class Meta:
        database = db

class Mark(Model):
    student = ForeignKeyField(Student, backref='marks')
    subject = ForeignKeyField(Subject, backref='marks')
    mark = IntegerField()

    class Meta:
        database = db

def list_students():
    students = Student.select()
    for student in students:
        print(student.name, student.birthdate)

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

if __name__ == "__main__":
    init_db()
    fill_db()
