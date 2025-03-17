import math as m

def f(x):
    return m.sqrt(x**2)

a = -2
b = 2
n = 4

dx = (b-a)/n
areal = 0

for i in range(n):
    x = a + i*dx
    areal += f(x)*dx

print(f"Arealet med {n} rektangler blir {areal:.1f}")