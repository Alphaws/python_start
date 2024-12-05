"""
Ez a program egy 52 lapos francia kártyapakliból véletlenszerűen oszt 5 lapot.
A program bemutatja a random választást és a lista kezelést.
"""

import random

def pakli_letrehozasa():
    """Létrehoz egy 52 lapos francia kártyapaklit."""
    szinek = ["♠", "♥", "♦", "♣"]
    ertekek = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    pakli = [(szin, ertek) for szin in szinek for ertek in ertekek]
    return pakli

def ot_lap_osztasa(pakli):
    """Véletlenszerűen kiválaszt 5 lapot a pakliból."""
    return random.sample(pakli, 5)

def lap_megjelenites(lap):
    """Egy kártya megjelenítése string formátumban."""
    szin, ertek = lap
    return f"{szin}{ertek}"

def main():
    # Pakli létrehozása
    pakli = pakli_letrehozasa()
    
    # 5 lap osztása
    osztott_lapok = ot_lap_osztasa(pakli)
    
    # Eredmény kiírása
    print("Az osztott lapok:")
    for lap in osztott_lapok:
        print(lap_megjelenites(lap), end=" ")
    print()

if __name__ == "__main__":
    main()
