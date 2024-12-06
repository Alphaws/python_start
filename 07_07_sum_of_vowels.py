"""
Ez a modul egy olyan függvényt tartalmaz, amely egy szövegben található magánhangzók
összegét számolja ki, ahol bizonyos magánhangzók számértékkel rendelkeznek.

Magánhangzók értékei:
A = 4
E = 3
I = 1
O = 0
U = 0
"""

def maganhangzok_osszege(szoveg: str) -> int:
    """
    Kiszámolja a szövegben található magánhangzók összegét.
    
    Args:
        szoveg: A feldolgozandó szöveg
        
    Returns:
        int: A magánhangzók számértékeinek összege
    """
    # Magánhangzók és értékeik definiálása
    maganhangzo_ertekek = {
        'a': 4,
        'e': 3,
        'i': 1,
        'o': 0,
        'u': 0
    }
    
    # Összeg inicializálása
    osszeg = 0
    
    # Végigmegyünk a szövegen és összegezzük a magánhangzók értékeit
    for karakter in szoveg.lower():
        if karakter in maganhangzo_ertekek:
            osszeg += maganhangzo_ertekek[karakter]
            
    return osszeg


# Tesztesetek
if __name__ == "__main__":
    tesztesetek = [
        "Let\'s test this function.",
        "I love edabit!",
        "hello",
        "python",
        "Tökéletlenek",
        "Árvíztűrő tükörfúrógép",
        "",
    ]
    
    for teszt in tesztesetek:
        eredmeny = maganhangzok_osszege(teszt)
        print(f"Szöveg: {teszt:10} | Magánhangzók összege: {eredmeny}")
