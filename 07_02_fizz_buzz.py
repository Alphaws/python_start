"""
FizzBuzz játék implementációja.
A program 1-től 100-ig kiírja a számokat, de:
- ha a szám osztható 3-mal, akkor 'Fizz'-t ír ki
- ha a szám osztható 5-tel, akkor 'Buzz'-t ír ki
- ha mindkettővel osztható, akkor 'FizzBuzz'-t ír ki
"""

def fizz_buzz(felso_hatar: int) -> None:
    """
    FizzBuzz sorozat generálása és kiírása.
    
    Args:
        felso_hatar: A sorozat felső határa (bezárólag)
    """
    # Végigmegyünk a számokon 1-től a felső határig
    for szam in range(1, felso_hatar + 1):
        # Az eredmény string kezdetben üres
        eredmeny = ""
        
        # Ha osztható 3-mal, hozzáadjuk a Fizz-t
        if szam % 3 == 0:
            eredmeny += "Fizz"
            
        # Ha osztható 5-tel, hozzáadjuk a Buzz-t
        if szam % 5 == 0:
            eredmeny += "Buzz"
            
        # Ha az eredmény üres maradt, akkor a számot írjuk ki
        if not eredmeny:
            eredmeny = str(szam)
            
        print(eredmeny)

if __name__ == "__main__":
    # Meghívjuk a függvényt 100-as felső határral
    fizz_buzz(100)
