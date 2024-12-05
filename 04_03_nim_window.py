"""
NIM játék grafikus felülettel
A játékosok felváltva vehetnek el 1-3 követ. Az veszít, aki az utolsó követ veszi el.
A kövek grafikusan is megjelennek emoji formájában.
"""

from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel,
                           QPushButton, QVBoxLayout, QHBoxLayout,
                           QWidget, QMessageBox)
from PyQt6.QtCore import Qt
import sys
import random

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Ablak beállításai
        self.setWindowTitle("NIM Játék")
        self.setFixedSize(600, 400)  # Nagyobb ablakméret a kövek megjelenítéséhez

        # Játék változók inicializálása
        self.kovek_szama = random.randint(15, 25)  # Kevesebb kő, hogy jobban látszódjon
        self.aktualis_jatekos = 1

        # Központi widget létrehozása
        kozponti_widget = QWidget()
        self.setCentralWidget(kozponti_widget)

        # Elrendezés beállítása
        elrendezes = QVBoxLayout()
        kozponti_widget.setLayout(elrendezes)

        # Játékállapot címke
        self.allapot_cimke = QLabel(f"Kövek száma: {self.kovek_szama}\n"
                                   f"{self.aktualis_jatekos}. játékos következik")
        self.allapot_cimke.setAlignment(Qt.AlignmentFlag.AlignCenter)
        elrendezes.addWidget(self.allapot_cimke)

        # Kövek megjelenítése
        self.kovek_cimke = QLabel()
        self.kovek_cimke.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.kovek_cimke.setWordWrap(True)  # Sortörés engedélyezése
        self.kovek_frissitese()
        elrendezes.addWidget(self.kovek_cimke)

        # Gombok létrehozása
        gombok_sora = QHBoxLayout()

        for i in range(1, 4):
            gomb = QPushButton(f"{i} kő elvétele")
            gomb.clicked.connect(lambda checked, x=i: self.kovek_elvetele(x))
            gombok_sora.addWidget(gomb)

        elrendezes.addLayout(gombok_sora)

    def kovek_frissitese(self):
        """Kövek grafikus megjelenítésének frissítése"""
        # 🪨 emoji használata a kövek megjelenítéséhez
        kovek_szoveg = "🪨 " * self.kovek_szama
        self.kovek_cimke.setText(kovek_szoveg)

    def kovek_elvetele(self, elvett_kovek):
        """Kövek elvétele és játékállapot frissítése"""
        if elvett_kovek <= self.kovek_szama:
            self.kovek_szama -= elvett_kovek

            # Kövek grafikus megjelenítésének frissítése
            self.kovek_frissitese()

            # Játék vége ellenőrzése
            if self.kovek_szama == 0:
                QMessageBox.information(self, "Játék vége",
                                      f"A {self.aktualis_jatekos}. játékos vesztett!")
                self.close()
                return

            # Következő játékos
            self.aktualis_jatekos = 2 if self.aktualis_jatekos == 1 else 1

            # Állapot frissítése
            self.allapot_cimke.setText(f"Kövek száma: {self.kovek_szama}\n"
                                      f"{self.aktualis_jatekos}. játékos következik")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
