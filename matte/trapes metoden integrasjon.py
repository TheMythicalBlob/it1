# Definere funksjonen som skal integreres
def f(x):
    return x**2

# Funksjon for trapesmetoden
def trapesmetoden(f, a, b, n):
    h = (b - a) / n  # Bredde på delintervallene
    summen = 0.5 * (f(a) + f(b))  # Starter med venstre- og høyreendepunkt
    for i in range(1, n):
        summen += f(a + i * h)
    return h * summen

# Brukerinput for integrasjonsgrenser og antall delintervaller
a = float(input("Skriv inn nedre grense for integrasjonen: "))
b = float(input("Skriv inn øvre grense for integrasjonen: "))
n = int(input("Skriv inn antall delintervaller: "))
 
# Beregne integralene med de tre metodene
trapes_resultat = trapesmetoden(f, a, b, n)
 
# Skrive ut resultatene
print(f"Trapesmetoden: {trapes_resultat}")
