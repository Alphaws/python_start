"""
Egyszerű hangeffektek generálása a Wizard of Wor játékhoz.
"""

import numpy as np
from scipy import wavfile

def lepes_hang():
    """Rövid, magas hangú lépés effekt"""
    sample_rate = 44100
    duration = 0.1
    t = np.linspace(0, duration, int(sample_rate * duration))
    frequency = 1000
    signal = np.sin(2 * np.pi * frequency * t) * 0.5
    # Fade out effektus
    fade = np.linspace(1.0, 0.0, len(signal))
    signal = signal * fade
    return sample_rate, (signal * 32767).astype(np.int16)

def utkozés_hang():
    """Mélyebb, hosszabb hang falnak ütközéskor"""
    sample_rate = 44100
    duration = 0.2
    t = np.linspace(0, duration, int(sample_rate * duration))
    frequency = 200
    signal = np.sin(2 * np.pi * frequency * t) * 0.7
    # Gyors fade in és fade out
    fade_in = np.linspace(0.0, 1.0, len(signal)//4)
    fade_out = np.linspace(1.0, 0.0, len(signal)-len(fade_in))
    fade = np.concatenate((fade_in, fade_out))
    signal = signal * fade
    return sample_rate, (signal * 32767).astype(np.int16)

def hatter_zene():
    """Egyszerű, ismétlődő háttérzene"""
    sample_rate = 44100
    duration = 2.0
    t = np.linspace(0, duration, int(sample_rate * duration))
    
    # Alap dallam
    f1, f2 = 200, 300
    signal = np.sin(2 * np.pi * f1 * t) * 0.3
    signal += np.sin(2 * np.pi * f2 * t) * 0.2
    
    # Pulzáló effektus
    pulse = np.sin(2 * np.pi * 2 * t) * 0.5 + 0.5
    signal = signal * pulse
    
    return sample_rate, (signal * 32767).astype(np.int16)

def main():
    """Hangfájlok létrehozása"""
    # Lépés hang
    rate, data = lepes_hang()
    wavfile.write('hangok/lepes.wav', rate, data)
    
    # Ütközés hang
    rate, data = utkozés_hang()
    wavfile.write('hangok/utkozés.wav', rate, data)
    
    # Háttérzene
    rate, data = hatter_zene()
    wavfile.write('hangok/hatter.wav', rate, data)

if __name__ == "__main__":
    main()
    print("Hangfájlok létrehozva a 'hangok' mappában!") 