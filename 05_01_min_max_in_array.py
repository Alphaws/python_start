import random

def main():
    szamok = [];
    for i in range(10):
        szamok.append(random.randint(1, 100))
    print(f"Számok: {szamok}")
    print(f"Minimum: {min(szamok)}")
    print(f"Maximum: {max(szamok)}")
    print(f"Összeg: {sum(szamok)}")
    print(f"Átlag: {sum(szamok) / len(szamok)}")


if __name__ == '__main__':
    main()
