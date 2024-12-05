import tkinter as tk
from tkinter import ttk

# Főablak létrehozása
ablak = tk.Tk()
ablak.title("Első ablakos program")

# Ablak méretének beállítása
ablak_szelesseg = 300
ablak_magassag = 200
ablak.geometry(f"{ablak_szelesseg}x{ablak_magassag}")

# Címke létrehozása a "Hello World" szöveggel
cimke = ttk.Label(ablak, text="Hello World!", font=("Arial", 14))
cimke.pack(expand=True)

# Az ablak középre pozicionálása a képernyőn
kepernyo_szelesseg = ablak.winfo_screenwidth()
kepernyo_magassag = ablak.winfo_screenheight()
x = (kepernyo_szelesseg - ablak_szelesseg) // 2
y = (kepernyo_magassag - ablak_magassag) // 2
ablak.geometry(f"+{x}+{y}")

# Főablak megjelenítése és eseménykezelő indítása
ablak.mainloop()
