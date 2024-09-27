import scipy.integrate as integrate
 
# Definere funksjonen f(x)
def f(x):
    return x**2
 
# Beregne det bestemte integralet med start og slutt verdi
resultat, _ = integrate.quad(f, 0, 2)
 
print(resultat)