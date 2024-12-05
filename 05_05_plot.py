"""
Ez a modul az x^2 függvény grafikus megjelenítését végzi matplotlib.pyplot használatával.
"""

import numpy as np
import matplotlib.pyplot as plt

def rajzol_negyzet_fuggveny():
    """
    Az x^2 függvény kirajzolása a [-10, 10] intervallumban.
    """
    # Létrehozunk egy x tengely értékkészletet
    x_ertekek = np.linspace(-10, 10, 200)
    
    # Kiszámoljuk az y értékeket (x^2)
    y_ertekek = x_ertekek ** 2
    
    # Létrehozzuk az ábrát
    plt.figure(figsize=(10, 6))
    
    # Kirajzoljuk a függvényt
    plt.plot(x_ertekek, y_ertekek, 'b-', label='f(x) = x²')
    
    # Beállítjuk a tengelyeket és a rácsot
    plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    plt.grid(True, alpha=0.3)
    
    # Címkék és feliratok hozzáadása
    plt.title('Az x² függvény grafikonja')
    plt.xlabel('x tengely')
    plt.ylabel('y tengely')
    plt.legend()
    
    # Megjelenítjük az ábrát
    plt.show()

if __name__ == "__main__":
    rajzol_negyzet_fuggveny()
