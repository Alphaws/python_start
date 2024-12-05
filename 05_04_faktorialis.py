"""
Ez a program kiszámítja a 100 faktoriálisát.
A faktoriális (n!) az összes n-nél kisebb vagy egyenlő pozitív egész szám szorzata.
Például: 5! = 5 * 4 * 3 * 2 * 1 = 120
"""
import time  # Időméréshez szükséges modul importálása

def szamol_rekurzivan(szam):
    if szam == 0 or szam == 1:
        return 1
    return szam * szamol_rekurzivan(szam - 1)

def szamold_faktorialis(szam):
    """
    Kiszámolja a megadott szám faktoriálisát.
    
    Args:
        szam: Az a pozitív egész szám, aminek a faktoriálisát számoljuk
        
    Returns:
        A szám faktoriálisa
    """
    if szam < 0:
        return "Negatív számnak nincs faktoriálisa"
    if szam == 0 or szam == 1:
        return 1
    
    eredmeny = 1
    for i in range(2, szam + 1):
        eredmeny *= i
    return eredmeny

def main():
    # A feladat: számoljuk ki a 100 faktoriálisát
    szam = 990

    start_time = time.time()
    eredmeny = szamold_faktorialis(szam)
    end_time = time.time()
    print(f"Iteratív megoldás futási ideje: {end_time - start_time:.6f} másodperc")
    
    start_time = time.time()
    eredmeny_rekurziv = szamol_rekurzivan(szam)
    end_time = time.time()
    print(f"Rekurzív megoldás futási ideje: {end_time - start_time:.6f} másodperc")
    
    #print(f"{szam}! értéke:")
    #print(eredmeny)
    #print(eredmeny_rekurziv)    
    
if __name__ == "__main__":
    main()
