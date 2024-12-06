import json
import os
from datetime import datetime
class LogHandler:
    def __init__(self, filename):
        self.filename = filename
        self.logData = {}
        self.read_log()

    def read_log(self):
        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r", encoding="utf-8") as log_file:
            self.logData = json.load(log_file)

    def write_log(self):
        with open(self.filename, "w", encoding="utf-8") as log_file:
            json.dump(self.logData, log_file, indent=4)

    def give_marks(self, student_name, mark):
        # Log format: {"Gipsz Jakab": [5, 4, 5, 2, 5]}
        if student_name not in self.logData:
            self.logData[student_name] = []
        self.logData[student_name].append(mark)
        self.logData[student_name].append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.write_log()


def demo_log():
    fizika = LogHandler("fizika.json")
    fizika.give_marks("Gipsz Jakab", 5)
    fizika.give_marks("Gipsz Jakab", 4)
    fizika.give_marks("Gipsz Jakab", 5)
    fizika.give_marks("Gipsz Jakab", 2)
    fizika.give_marks("Gipsz Jakab", 5)
    print(fizika.logData)


def write_to_file():
    outfile = open("outfile.txt", "w", encoding="utf-8")
    outfile.write("Kázmér füstölgő fűnyírót húz.")
    outfile.close()

    with open("outfile2.txt", "w", encoding="utf-8") as outfile:
        outfile.write("Kázmér füstölgő fűnyírót húz. De már le van nyírva a fű.")

def create_log():
    naplo = [
        {
            "diak": "Gipsz Jakab", 
            "osztaly": "10.A", 
            "jegyek": [5, 4, 5, 2, 5]
        },
        {
            "diak": "Mézga Géza", 
            "osztaly": "10.A", 
            "jegyek": [4, 2, 5, 1, 5]
        }
    ]
    with open("naplo.txt", "w", encoding="utf-8") as naplo_file:
        naplo_file.write(json.dumps(naplo, indent=4))

def read_log():
    with open("naplo.txt", "r", encoding="utf-8") as naplo_file:
        naplo = json.load(naplo_file)
        print(naplo)
    return naplo

def main():
    write_to_file()
    create_log()
    read_log()
    demo_log()

if __name__ == "__main__":
    main()
