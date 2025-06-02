import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Data
datat = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])
datay = np.array([190, 148, 132, 152, 192, 223, 199, 160, 139, 152, 198, 231, 224])

t = datat
y = datay

# Definer sinus-funksjonen med en generell frekvensparameter
def h(t, A, omega, phi, d):
    return A * np.sin(omega * t + phi) + d

# Utfør kurvetilpasning
# Gode startverdier: Amplitude, omega (frekvens), faseforskyvning, vertikal forskyvning
initial_guess = [50, 0.5, 0, np.mean(y)]  # Justerte startverdier
popt, _ = curve_fit(h, t, y, p0=initial_guess)
A, omega, phi, d = popt

# Print resultatene
print(f"A (amplitude): {A}")
print(f"omega (frekvens): {omega}")
print(f"phi (faseforskyvning): {phi}")
print(f"d (vertikal forskyvning): {d}")

# Tegn dataene som punkter
plt.plot(t, y, "o", label="Data", color="blue")

# Tegn den tilpassede sinuskurven
t2 = np.linspace(min(t), max(t), 1000)  # Tett tidsområde for en jevn kurve
plt.plot(t2, h(t2, A, omega, phi, d), label="Sinusregresjon", color="red")

# Tilpass plotutseende
plt.tick_params(axis="y", labelsize=20)
plt.tick_params(axis="x", labelsize=20)
plt.xlabel("Tid (s)", fontsize=20)
plt.ylabel("Høyde (cm)", fontsize=20)
plt.title("Sinusregresjon av data")
plt.legend()
plt.grid(True)
plt.show()
