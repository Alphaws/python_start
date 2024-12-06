import json

def write_to_file():
    outfile = open("outfile.txt", "w", encoding="utf-8")
    outfile.write("Kázmér füstölgő fűnyírót húz.")
    outfile.close()

    with open("outfile2.txt", "w", encoding="utf-8") as outfile:
        outfile.write("Kázmér füstölgő fűnyírót húz. De már le van nyírva a fű.")

def create_log():
    naplo = [
        {
            "diák": "Gipsz Jakab", 
            "osztály": "10.A", 
            "jegyek": [5, 4, 5, 2, 5]
        },
        {
            "diák": "Mézga Géza", 
            "osztály": "10.A", 
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
if __name__ == "__main__":
    main()
