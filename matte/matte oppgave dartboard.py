import numpy as np

# Sentrum på darttavlen
senter_x, senter_y = 100, 173
radius = 22.5

# Startpunkt for første pil
x, y = 30, 50

treff = 0

k = 1.2

for _ in range(20):
    # Beregner avstand til tavlens sentrum
    distanse = np.sqrt((x - senter_x) ** 2 + (y - senter_y) ** 2)
    
    # Sjekk om pilen treffer tavlen
    if distanse <= radius:
        treff += 1
    x += 10
    y *= k

print(treff)
