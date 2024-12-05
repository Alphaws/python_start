import random

def main():
    print("Hello, NIM játékos!")
    gyufak = random.randint(40, 60)
    print(f"A játékosoknak {gyufak} gyufája van a kupacban.")

    while gyufak > 0:
        jatekos_huzas = int(input("Húzz gyufát! (1-3): "))
        while jatekos_huzas < 1 or jatekos_huzas > 3:
            print("Nem érvényes húzás! A számnak 1 és 3 között kell lennie.")
            jatekos_huzas = int(input("Húzz gyufát! (1-3): "))
        
        gyufak -= jatekos_huzas
        print(f"Elvettél {jatekos_huzas} gyufát. A kupacban {gyufak} gyufa maradt.")
        if gyufak > 0:
            gep_huzas = random.randint(1, 3)
            gyufak -= gep_huzas
            print(f"A gép {gep_huzas} gyufát húzott. A kupacban {gyufak} gyufa maradt.")
            if gyufak <= 0:
                print("A gép vesztett!")
                break
        else:
            print("A játékos vesztett!")
            break
    print("A játéknak vége!")
    
if __name__ == "__main__":
    main() 