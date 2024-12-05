import random

# Bekérjük a játékos dobását
jatekos_dobas = int(input("Add meg a dobásod (1-6): "))

# Ellenőrizzük, hogy érvényes-e a dobás
if jatekos_dobas < 1 or jatekos_dobas > 6:
    print("Érvénytelen dobás! A számnak 1 és 6 között kell lennie.")
else:
    # Gép dobása (véletlenszerű szám 1 és 6 között)
    gep_dobas = random.randint(1, 6)
    
    # Kiírjuk mindkét dobást
    print(f"A te dobásod: {jatekos_dobas}")
    print(f"A gép dobása: {gep_dobas}")
    
    # Eredmény meghatározása és kiírása
    if jatekos_dobas > gep_dobas:
        print("Gratulálok, te nyertél!")
    elif gep_dobas > jatekos_dobas:
        print("A gép nyert!")
    else:
        print("Döntetlen!") 