import math

def beregn_volum(n):
    total = 0.0
    delta_x = 2.0 / n
    for i in range(1, n + 1):
        x_i = (i - 0.5) * delta_x
        total += math.exp(-2 * x_i ** 2)
    volum = math.pi * delta_x * total
    return volum

n = 1000 
volum = beregn_volum(n)
print(f"Volumet er approximert til {volum:.4f}")