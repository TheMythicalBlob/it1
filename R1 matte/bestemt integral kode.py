import scipy.integrate as integrate
 
# Definere funksjonen f(x)
def f(x):
    return 0.0006*x**4 - 0.07*x**3 + 2.2*x**2 - 8.2*x + 22
 
# Beregne det bestemte integralet fra 0 til 52
resultat, _ = integrate.quad(f, 0, 52)
 
print(resultat)