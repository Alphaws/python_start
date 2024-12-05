"""
Ez a modul egy függvényt tartalmaz, amely egy számlistából kiszámítja a páros és páratlan számok összegét.
A függvény egy kételemű listával tér vissza, ahol az első elem a páros számok összege,
a második elem pedig a páratlan számok összege.
"""

def szamok_osszege(szamlista):
    """
    Kiszámítja egy számlistában a páros és páratlan számok összegét.
    
    Args:
        szamlista (list): Számok listája
        
    Returns:
        list: Kételemű lista [páros_összeg, páratlan_összeg]
    """
    # Kezdőértékek beállítása
    paros_osszeg = 0
    paratlan_osszeg = 0
    
    # Végigmegyünk a lista elemein
    for szam in szamlista:
        if szam % 2 == 0:
            # Ha páros a szám, hozzáadjuk a párosok összegéhez
            paros_osszeg += szam
        else:
            # Ha páratlan a szám, hozzáadjuk a páratlanok összegéhez
            paratlan_osszeg += szam
    
    return [paros_osszeg, paratlan_osszeg]


# Tesztesetek a függvény működésének ellenőrzésére
if __name__ == "__main__":
    # Tesztlista létrehozása
    teszt_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    
    # Függvény meghívása és eredmény kiírása
    eredmeny = szamok_osszege(teszt_lista)
    print(f"A páros számok összege: {eredmeny[0]}")
    print(f"A páratlan számok összege: {eredmeny[1]}")
