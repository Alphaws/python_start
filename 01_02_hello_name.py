def get_name():
    name = input("Kérem adja meg a nevét: ")
    return name

def greet_person(name):
    print(f"Üdvözlöm, {name}!")

def main():
    name = get_name()
    greet_person(name)

if __name__ == "__main__":
    main() 