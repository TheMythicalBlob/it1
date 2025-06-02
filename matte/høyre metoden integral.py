# Definere funksjonen som skal integreres
def f(x):
    return 0.0006*x**4 - 0.07*x**3 + 2.2*x**2 - 8.2*x + 22

 
# Funksjon for høyremetoden
def høyremetoden(f, a, b, n):
    h = (b - a) / n  # Bredde på delintervallene
    summen = 0
    for i in range(1, n + 1):
        summen += f(a + i * h)
    return h * summen


# Brukerinput for integrasjonsgrenser og antall delintervaller
a = float(input("Skriv inn nedre grense for integrasjonen: "))
b = float(input("Skriv inn øvre grense for integrasjonen: "))
n = int(input("Skriv inn antall delintervaller: "))
 
# Beregne integralene med de tre metodene
høyre_resultat = høyremetoden(f, a, b, n)
 
# Skrive ut resultatene
print(f"Høyremetoden: {høyre_resultat}")

