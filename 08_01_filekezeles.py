import json
import os
import datetime
import pickle


class Student:
    def __init__(self, id_p, name, birthdate):
        self.name = name
        self.birthdate = birthdate
        self.id = id_p

class StudentList:
    def __init__(self, filename):
        self.students = []
        self.filename = filename
        self.next_id = 1
        self.read_students()

    def read_students(self):
        if not os.path.exists(self.filename):
            return
        with open(self.filename, "rb") as file:
            self.students = pickle.load(file)
        self.next_id = max([student.id for student in self.students]) + 1

    def write_students(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self.students, file)

    def add_student(self, name, birthdate):
        new_student = Student(self.next_id, name, birthdate)
        self.students.append(new_student)
        self.next_id += 1
        self.write_students()
        return new_student


class LogHandler:
    def __init__(self, log_filename):
        self.log_filename = log_filename
        self.log_data = {}
        self.read_log()

    def write_log(self):
        with open(self.log_filename, "w", encoding="utf-8") as log_file:
            log_file.write(json.dumps(self.log_data))

    def read_log(self):
        if not os.path.exists(self.log_filename):
            return
        with open(self.log_filename, "r", encoding="utf-8") as log_file:
            self.log_data = json.loads(log_file.read())

    def give_mark(self, student_obj, mark):
        # Log format: {"Gipsz Jakab": [4, 5, 3, 2, 5, 5]}
        if student_obj.id not in self.log_data:
            self.log_data[student_obj.id] = []
        self.log_data[student_obj.id].append(mark)
        self.log_data[student_obj.id].append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.write_log()


subjects = ["fizika", "matek", "magyar"]


class ClassLog:
    def __init__(self, class_name):
        self.class_name = class_name
        os.makedirs(class_name, exist_ok=True)
        self.logs = {subject: LogHandler(f"{class_name}/{subject}.json") for subject in subjects}

    def give_mark(self, subject, student_obj, mark):
        if subject not in self.logs:
            print(f"Subject {subject} not found")
            return
        self.logs[subject].give_mark(student_obj, mark)

def demo_log():
    student_list = StudentList("students.pkl")
    gipsz_jakab = student_list.add_student("Gipsz Jakab", "2000-01-01")
    kis_gabor = student_list.add_student("Kis Gabor", "2000-01-02")
    toth_benedek = student_list.add_student("Toth Benedek", "2000-01-03")
    nagy_peter = student_list.add_student("Nagy Peter", "2000-01-04")
    class_log = ClassLog("7.B")
    class_log.give_mark("fizika", gipsz_jakab, 4)
    class_log.give_mark("fizika", gipsz_jakab, 5)
    class_log.give_mark("fizika", gipsz_jakab, 3)
    class_log.give_mark("matek", gipsz_jakab, 5)
    class_log.give_mark("matek", gipsz_jakab, 5)
    class_log.give_mark("matek", gipsz_jakab, 5)
    class_log.give_mark("magyar", gipsz_jakab, 5)
    class_log.give_mark("magyar", gipsz_jakab, 5)
    class_log.give_mark("magyar", gipsz_jakab, 5)

def write_to_file():
    with open("outfile.txt", "w", encoding="utf-8") as outfile:
        outfile.write("Kázmér füstölgő fűnyírót húz. Árvíztűrő tükörfúrógép!")
    # itt mar nincs outfile

def read_from_file():
    with open("outfile.txt", "r", encoding="utf-8") as infile:
        print(infile.read())

def create_log():
    naplo = [
        {"diak": "Gipsz Jakab", "jegyek": [4, 5, 3, 2, 5, 5]},
        {"diak": "Kis Gabor", "jegyek": [3, 3, 3, 3, 3, 3]},
        {"diak": "Toth Benedek", "jegyek": [5, 5, 5, 5, 5, 5]},
        {"diak": "Nagy Peter", "jegyek": [2, 2, 2, 2, 2, 2]}
    ]
    with open("naplo.txt", "w", encoding="utf-8") as naplo_file:
        naplo_file.write(json.dumps(naplo, indent=4))

def read_log():
    with open("naplo.txt", "r", encoding="utf-8") as naplo_file:
        print(json.loads(naplo_file.read()))

if __name__ == "__main__":
    demo_log()
