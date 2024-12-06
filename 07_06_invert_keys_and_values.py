"""
Ez a modul egy szótár kulcsainak és értékeinek felcserélését végző függvényt tartalmaz.

A modul fő funkciója:
- Egy szótár kulcsainak és értékeinek megfordítása, ahol az eredeti értékek lesznek 
  az új kulcsok és az eredeti kulcsok lesznek az új értékek
"""

def invert_keys_and_values(dict1):
    """
    Megfordítja egy szótár kulcsait és értékeit.
    
    Args:
        dict1 (dict): A bemeneti szótár, amelynek kulcsait és értékeit fel szeretnénk cserélni
        
    Returns:
        dict: Egy új szótár, ahol az eredeti szótár értékei a kulcsok és a kulcsai az értékek
        
    Példa:
        >>> invert_keys_and_values({"a": 1, "b": 2, "c": 3})
        {1: 'a', 2: 'b', 3: 'c'}
    """
    return {value: key for key, value in dict1.items()}

# Példa a függvény használatára
print(invert_keys_and_values({"egy": 1, "ketto": 2, "harom": 3}))