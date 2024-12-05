from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import Qt
import sys

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        
        # Ablak címének és méretének beállítása
        self.setWindowTitle("Hello World")
        self.setFixedSize(400, 200)
        
        # Címke létrehozása és beállítása
        label = QLabel("Hello, World!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Betűméret növelése
        font = label.font()
        font.setPointSize(24)
        label.setFont(font)
        
        # Címke beállítása központi widgetként
        self.setCentralWidget(label)

def main():
    # QApplication példány létrehozása
    app = QApplication(sys.argv)
    
    # Főablak létrehozása és megjelenítése
    window = MainWindow()
    window.show()
    
    # Alkalmazás futtatása
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
   