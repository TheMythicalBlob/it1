import numpy as np

# Definere funksjonen som skal integreres
def f(x):
    return 0.0006*x**4 - 0.07*x**3 + 2.2*x**2 - 8.2*x + 22
 
# Funksjon for venstremetoden
def venstremetoden(f, a, b, n):
    h = (b - a) / n  # Bredde på delintervallene
    summen = 0
    for i in range(n):
        summen += f(a + i * h)
    return h * summen
 
# Funksjon for høyremetoden
def høyremetoden(f, a, b, n):
    h = (b - a) / n  # Bredde på delintervallene
    summen = 0
    for i in range(1, n + 1):
        summen += f(a + i * h)
    return h * summen
 
# Funksjon for trapesmetoden
def trapesmetoden(f, a, b, n):
    h = (b - a) / n  # Bredde på delintervallene
    summen = 0.5 * (f(a) + f(b))  # Starter med venstre- og høyreendepunkt
    for i in range(1, n):
        summen += f(a + i * h)
    return h * summen
 
# Definer integrasjonsgrenser og antall delintervaller
a = 0  # Nedre grense
b = 52  # Øvre grense
n = 1000  # Antall delintervaller
 
# Beregne integralene med de tre metodene
venstre_resultat = venstremetoden(f, a, b, n)
høyre_resultat = høyremetoden(f, a, b, n)
trapes_resultat = trapesmetoden(f, a, b, n)
 
# Skrive ut resultatene
print(f"Venstremetoden: {venstre_resultat}")
print(f"Høyremetoden: {høyre_resultat}")
print(f"Trapesmetoden: {trapes_resultat}")