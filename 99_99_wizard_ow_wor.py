"""
Wizard of Wor játék implementációja Pygame használatával.
A játék a Commodore 64-es klasszikus alapján készült.
"""

import pygame
import sys
import os
import random

class Lovedek:
    """Lövedék osztály a játékos lövéseinek kezeléséhez"""
    def __init__(self, x, y, irany):
        self.x = x
        self.y = y
        self.irany = irany  # "BAL", "JOBB", "FEL", "LE"
        self.sebesseg = 10
        self.meret = 5
        self.aktiv = True
    
    def mozgas(self, falak):
        """Lövedék mozgatása és ütközésvizsgálat"""
        if not self.aktiv:
            return False
            
        if self.irany == "BAL":
            self.x -= self.sebesseg
        elif self.irany == "JOBB":
            self.x += self.sebesseg
        elif self.irany == "FEL":
            self.y -= self.sebesseg
        elif self.irany == "LE":
            self.y += self.sebesseg
            
        # Ütközésvizsgálat falakkal
        lovedek_teglalap = pygame.Rect(self.x, self.y, self.meret, self.meret)
        if any(lovedek_teglalap.colliderect(fal) for fal in falak):
            self.aktiv = False
            return False
        return True
        
    def rajzol(self, ablak):
        """Lövedék megjelenítése"""
        if self.aktiv:
            pygame.draw.rect(ablak, (255, 255, 0), (self.x, self.y, self.meret, self.meret))

class Jatekos:
    def __init__(self, x, y, meret, hangok):
        """
        Játékos inicializálása
        x, y: kezdő pozíció
        meret: játékos mérete pixelben
        hangok: játék hangeffektek szótára
        """
        self.x = x
        self.y = y
        self.meret = meret
        self.sebesseg = 5
        self.hangok = hangok
        self.utolso_lepes_ido = 0
        self.irany = "JOBB"  # Alapértelmezett irány
        self.lovedekek = []  # Aktív lövedékek listája
        self.utolso_loves_ido = 0
        self.loves_kesleltetés = 500  # ms
        
    def loves(self, aktualis_ido):
        """Új lövedék létrehozása"""
        if aktualis_ido - self.utolso_loves_ido < self.loves_kesleltetés:
            return
            
        # Lövedék pozíciójának kiszámítása a játékos közepéről
        loves_x = self.x + self.meret // 2 - 2
        loves_y = self.y + self.meret // 2 - 2
        
        self.lovedekek.append(Lovedek(loves_x, loves_y, self.irany))
        self.utolso_loves_ido = aktualis_ido
        
    def mozgas(self, irany, falak):
        """Játékos mozgatása és ütközésvizsgálat"""
        uj_x = self.x
        uj_y = self.y
        self.irany = irany  # Irány mentése a lövéshez
        
        if irany == "BAL":
            uj_x -= self.sebesseg
        elif irany == "JOBB":
            uj_x += self.sebesseg
        elif irany == "FEL":
            uj_y -= self.sebesseg
        elif irany == "LE":
            uj_y += self.sebesseg
            
        # Ütközésvizsgálat a falakkal
        jatekos_teglalap = pygame.Rect(uj_x, uj_y, self.meret, self.meret)
        if not any(jatekos_teglalap.colliderect(fal) for fal in falak):
            self.x = uj_x
            self.y = uj_y
            # Lépés hang lejátszása időzítéssel
            aktualis_ido = pygame.time.get_ticks()
            if aktualis_ido - self.utolso_lepes_ido > 200:  # 200ms késleltetés
                self.hangok['lepes'].play()
                self.utolso_lepes_ido = aktualis_ido
        else:
            # Falnak ütközés hang
            self.hangok['utkozés'].play()

    def update(self, falak):
        """Lövedékek frissítése"""
        self.lovedekek = [l for l in self.lovedekek if l.mozgas(falak)]
        
    def rajzol(self, ablak):
        """Játékos és lövedékek megjelenítése"""
        pygame.draw.rect(ablak, (255, 255, 0), (self.x, self.y, self.meret, self.meret))
        for lovedek in self.lovedekek:
            lovedek.rajzol(ablak)

class Ellenseg:
    """Ellenség osztály"""
    def __init__(self, x, y, meret):
        self.x = x
        self.y = y
        self.meret = meret
        self.sebesseg = 3
        self.szin = (255, 0, 0)  # Piros
        self.iranyok = ["BAL", "JOBB", "FEL", "LE"]
        self.irany = random.choice(self.iranyok)
        self.iranyvaltas_ido = 0
        self.iranyvaltas_intervallum = 1000  # ms
        
    def mozgas(self, falak, aktualis_ido):
        """Ellenség mozgatása és ütközésvizsgálat"""
        # Irányváltás időnként
        if aktualis_ido - self.iranyvaltas_ido > self.iranyvaltas_intervallum:
            self.irany = random.choice(self.iranyok)
            self.iranyvaltas_ido = aktualis_ido
            
        uj_x = self.x
        uj_y = self.y
        
        if self.irany == "BAL":
            uj_x -= self.sebesseg
        elif self.irany == "JOBB":
            uj_x += self.sebesseg
        elif self.irany == "FEL":
            uj_y -= self.sebesseg
        elif self.irany == "LE":
            uj_y += self.sebesseg
            
        # Ütközésvizsgálat falakkal
        ellenseg_teglalap = pygame.Rect(uj_x, uj_y, self.meret, self.meret)
        if not any(ellenseg_teglalap.colliderect(fal) for fal in falak):
            self.x = uj_x
            self.y = uj_y
        else:
            # Ha falnak ütközik, váltson irányt
            self.irany = random.choice(self.iranyok)
            
    def rajzol(self, ablak):
        """Ellenség megjelenítése"""
        pygame.draw.rect(ablak, self.szin, (self.x, self.y, self.meret, self.meret))
        
    def talalat_vizsgalat(self, lovedek):
        """Ellenőrzi, hogy eltalálta-e egy lövedék"""
        ellenseg_teglalap = pygame.Rect(self.x, self.y, self.meret, self.meret)
        lovedek_teglalap = pygame.Rect(lovedek.x, lovedek.y, lovedek.meret, lovedek.meret)
        return ellenseg_teglalap.colliderect(lovedek_teglalap)

class WizardOfWor:
    def __init__(self):
        # Pygame és mixer inicializálása
        pygame.init()
        pygame.mixer.init()
        
        # Hangok betöltése
        self.hangok = {
            'lepes': self.hang_betoltes('lepes.wav'),
            'utkozés': self.hang_betoltes('utkozés.wav'),
            'hatter': self.hang_betoltes('hatter.wav')
        }
        
        # Háttérzene indítása
        self.hangok['hatter'].play(-1)  # -1: végtelen ismétlés
        
        # Képernyő beállítások
        self.ABLAK_SZELESSEG = 800
        self.ABLAK_MAGASSAG = 600
        self.FEKETE = (0, 0, 0)
        self.SARGA = (255, 255, 0)
        self.KEK = (0, 0, 150)
        
        # Játékablak létrehozása
        self.ablak = pygame.display.set_mode((self.ABLAK_SZELESSEG, self.ABLAK_MAGASSAG))
        pygame.display.set_caption("Wizard of Wor - Réfi Edition")
        
        # Játék óra
        self.ora = pygame.time.Clock()
        self.FPS = 60
        
        # Labirintus beállítások
        self.CELLA_MERET = 40
        self.LABIRINTUS = [
            "WWWWWWWWWWWWWWWWWWWW",
            "W    W     W    W  W",
            "W WW W WWW W WW    W",
            "W    W W W W    WW W",
            "WWW    W W    W    W",
            "W    WWW W WWW  W  W",
            "W WW  W   W    WW  W",
            "W    WW W   WW     W",
            "W WW    WWW    WW  W",
            "W    WW     WW     W",
            "WWWWWWWWWWWWWWWWWWWW"
        ]
        
        # Játékos létrehozása a labirintus közepén
        kezdo_x = (self.ABLAK_SZELESSEG - len(self.LABIRINTUS[0]) * self.CELLA_MERET) // 2
        kezdo_y = (self.ABLAK_MAGASSAG - len(self.LABIRINTUS) * self.CELLA_MERET) // 2
        jatekos_x = kezdo_x + 10 * self.CELLA_MERET  # középre helyezés
        jatekos_y = kezdo_y + 5 * self.CELLA_MERET   # középre helyezés
        self.jatekos = Jatekos(jatekos_x, jatekos_y, self.CELLA_MERET - 10, self.hangok)
        self.falak = []  # Falak tárolása ütközésvizsgálathoz
        
        # Pontszám beállítások
        self.pontszam = 0
        self.betutipus = pygame.font.Font(None, 36)  # Alapértelmezett betűtípus
        self.ELLENSEG_PONT = 100  # Pont egy ellenség lelövéséért
        self.SZINT = 1  # Játék szintje
        
        # Ellenségek létrehozása
        self.ellensegek = []
        self.ellenseg_letrehozas()
        
    def hang_betoltes(self, fajlnev):
        """Hang betöltése a hangok mappából"""
        try:
            hang_ut = os.path.join('hangok', fajlnev)
            hang = pygame.mixer.Sound(hang_ut)
            hang.set_volume(0.3)  # hangerő beállítása
            return hang
        except:
            # Ha nem sikerül betölteni, üres hang objektumot hozunk létre
            print(f"Nem sikerült betölteni a hangot: {fajlnev}")
            return pygame.mixer.Sound(buffer=bytes([0]))
            
    def jatek_leallitas(self):
        """Játék leállítása, erőforrások felszabadítása"""
        for hang in self.hangok.values():
            hang.stop()
        pygame.mixer.quit()
        pygame.quit()
        sys.exit()
        
    def rajzol_labirintus(self):
        """Labirintus kirajzolása"""
        self.falak = []  # Falak listájának törlése
        kezdo_x = (self.ABLAK_SZELESSEG - len(self.LABIRINTUS[0]) * self.CELLA_MERET) // 2
        kezdo_y = (self.ABLAK_MAGASSAG - len(self.LABIRINTUS) * self.CELLA_MERET) // 2
        
        for sor_index, sor in enumerate(self.LABIRINTUS):
            for oszlop_index, cella in enumerate(sor):
                x = kezdo_x + oszlop_index * self.CELLA_MERET
                y = kezdo_y + sor_index * self.CELLA_MERET
                
                if cella == 'W':  # Fal
                    fal_teglalap = pygame.Rect(x, y, self.CELLA_MERET, self.CELLA_MERET)
                    self.falak.append(fal_teglalap)
                    pygame.draw.rect(self.ablak, self.SARGA, fal_teglalap, 2)

    def ellenseg_letrehozas(self):
        """Ellenségek létrehozása random pozíciókban"""
        # Ellenségek számának növelése szintenként
        ellenseg_szam = 3 + self.SZINT - 1
        
        for _ in range(ellenseg_szam):  # Több ellenség magasabb szinten
            while True:
                # Random pozíció keresése
                sor = random.randint(1, len(self.LABIRINTUS)-2)
                oszlop = random.randint(1, len(self.LABIRINTUS[0])-2)
                
                if self.LABIRINTUS[sor][oszlop] == ' ':  # Ha üres hely
                    kezdo_x = (self.ABLAK_SZELESSEG - len(self.LABIRINTUS[0]) * self.CELLA_MERET) // 2
                    kezdo_y = (self.ABLAK_MAGASSAG - len(self.LABIRINTUS) * self.CELLA_MERET) // 2
                    
                    x = kezdo_x + oszlop * self.CELLA_MERET
                    y = kezdo_y + sor * self.CELLA_MERET
                    
                    self.ellensegek.append(Ellenseg(x, y, self.CELLA_MERET - 10))
                    break
    
    def kovetkezo_szint(self):
        """Következő szintre lépés"""
        self.SZINT += 1
        # Ellenségek sebességének növelése szintenként
        for ellenseg in self.ellensegek:
            ellenseg.sebesseg = 3 + (self.SZINT - 1) * 0.5
        
    def pontszam_kirajzolas(self):
        """Pontszám és szint megjelenítése"""
        # Pontszám szöveg
        pontszam_szoveg = f"Pontszám: {self.pontszam}"
        pontszam_felulet = self.betutipus.render(pontszam_szoveg, True, self.SARGA)
        self.ablak.blit(pontszam_felulet, (10, 10))
        
        # Szint szöveg
        szint_szoveg = f"Szint: {self.SZINT}"
        szint_felulet = self.betutipus.render(szint_szoveg, True, self.SARGA)
        szint_x = self.ABLAK_SZELESSEG - szint_felulet.get_width() - 10
        self.ablak.blit(szint_felulet, (szint_x, 10))
        
    def jatek_inditasa(self):
        """Fő játékciklus"""
        try:
            while True:
                aktualis_ido = pygame.time.get_ticks()
                
                for esemeny in pygame.event.get():
                    if esemeny.type == pygame.QUIT:
                        self.jatek_leallitas()
                
                # Billentyűzet kezelése
                billentyuk = pygame.key.get_pressed()
                if billentyuk[pygame.K_LEFT]:
                    self.jatekos.mozgas("BAL", self.falak)
                if billentyuk[pygame.K_RIGHT]:
                    self.jatekos.mozgas("JOBB", self.falak)
                if billentyuk[pygame.K_UP]:
                    self.jatekos.mozgas("FEL", self.falak)
                if billentyuk[pygame.K_DOWN]:
                    self.jatekos.mozgas("LE", self.falak)
                if billentyuk[pygame.K_SPACE]:
                    self.jatekos.loves(aktualis_ido)
                
                # Játékos és lövedékek frissítése
                self.jatekos.update(self.falak)
                
                # Ellenségek mozgatása
                for ellenseg in self.ellensegek:
                    ellenseg.mozgas(self.falak, aktualis_ido)
                
                # Lövedék-ellenség ütközés vizsgálata
                for lovedek in self.jatekos.lovedekek[:]:
                    for ellenseg in self.ellensegek[:]:
                        if ellenseg.talalat_vizsgalat(lovedek):
                            self.ellensegek.remove(ellenseg)
                            lovedek.aktiv = False
                            # Pontszám növelése
                            self.pontszam += self.ELLENSEG_PONT * self.SZINT
                            # Ha minden ellenség meghalt
                            if not self.ellensegek:
                                self.kovetkezo_szint()
                                self.ellenseg_letrehozas()
                
                # Képernyő törlése és rajzolás
                self.ablak.fill(self.KEK)
                self.rajzol_labirintus()
                self.jatekos.rajzol(self.ablak)
                
                # Ellenségek rajzolása
                for ellenseg in self.ellensegek:
                    ellenseg.rajzol(self.ablak)
                
                # Pontszám kirajzolása
                self.pontszam_kirajzolas()
                
                pygame.display.flip()
                self.ora.tick(self.FPS)
                
        except Exception as e:
            print(f"Hiba történt: {e}")
            self.jatek_leallitas()

if __name__ == "__main__":
    jatek = WizardOfWor()
    jatek.jatek_inditasa()
