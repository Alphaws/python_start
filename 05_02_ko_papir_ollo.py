"""
Kő-papír-olló játék

Ez a program egy egyszerű kő-papír-olló játékot valósít meg, ahol a felhasználó
a számítógép ellen játszhat. A program magyar nyelvű, és követi a játék
klasszikus szabályait.

Készítette: Claude AI
Verzió: 1.0
"""

import random

def jatekos_valasztas():
    """
    Bekéri és ellenőrzi a játékos választását.
    
    Returns:
        str: A játékos érvényes választása (ko/papir/ollo)
    """
    while True:
        valasztas = input("Válassz (ko/papir/ollo): ").lower().strip()
        if valasztas in ["ko", "papir", "ollo"]:
            return valasztas
        print("Érvénytelen választás! Kérlek válassz: ko, papir vagy ollo")

def gep_valasztas():
    """
    Generálja a számítógép véletlenszerű választását.
    
    Returns:
        str: A számítógép választása (ko/papir/ollo)
    """
    return random.choice(["ko", "papir", "ollo"])

def gyoztes_meghatarozas(jatekos, gep):
    """
    Meghatározza a kör győztesét.
    
    Args:
        jatekos (str): A játékos választása
        gep (str): A számítógép választása
        
    Returns:
        str: Az eredmény ("Játékos nyert", "Gép nyert" vagy "Döntetlen")
    """
    if jatekos == gep:
        return "Döntetlen"
    
    nyero_kombinaciok = {
        "ko": "ollo",
        "papir": "ko",
        "ollo": "papir"
    }
    
    if nyero_kombinaciok[jatekos] == gep:
        return "Játékos nyert"
    return "Gép nyert"

def jatek():
    """
    A játék fő logikája, amely kezeli a játékmenetet és a pontszámokat.
    """
    jatekos_pontszam = 0
    gep_pontszam = 0
    
    print("\nÜdvözöllek a Kő-Papír-Olló játékban!")
    print("A kilépéshez írd be: 'vege'\n")
    
    while True:
        # Játékos választása
        valasztas = input("\nVálassz (ko/papir/ollo vagy vege): ").lower().strip()
        if valasztas == "vege":
            break
            
        if valasztas not in ["ko", "papir", "ollo"]:
            print("Érvénytelen választás! Kérlek válassz: ko, papir vagy ollo")
            continue
            
        # Gép választása
        gep = gep_valasztas()
        
        # Eredmények kiírása
        print(f"\nTe választásod: {valasztas}")
        print(f"Gép választása: {gep}")
        
        # Győztes meghatározása
        eredmeny = gyoztes_meghatarozas(valasztas, gep)
        print(f"Eredmény: {eredmeny}")
        
        # Pontszámok frissítése
        if eredmeny == "Játékos nyert":
            jatekos_pontszam += 1
        elif eredmeny == "Gép nyert":
            gep_pontszam += 1
            
        # Aktuális állás kiírása
        print(f"\nÁllás: Játékos: {jatekos_pontszam} - Gép: {gep_pontszam}")

    # Végeredmény kiírása
    print("\n--- Játék vége ---")
    print(f"Végeredmény: Játékos: {jatekos_pontszam} - Gép: {gep_pontszam}")
    if jatekos_pontszam > gep_pontszam:
        print("Gratulálok, te nyertél!")
    elif jatekos_pontszam < gep_pontszam:
        print("A gép nyert!")
    else:
        print("Döntetlen!")

if __name__ == "__main__":
    jatek()
