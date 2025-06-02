import math as m

a = 8 # Startverdien til a(n)
n = 2 # Må starte her siden formelen fungerer bare for n>=2

# Koden må kjøre til n = 9 fordi da regnes det ut n = 10 siden python liker å telle med 0
while n < 9:
    a += 3*a-2*a-1-3
    n += 1

print(a)