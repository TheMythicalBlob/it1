# Beregne de første 30 tallene i rekursiv formel
def beregn_sum(antall_verdier):
    a = [1]  # Startverdi a_0 = 1
    for n in range(1, antall_verdier):
        neste_verdi = a[-1] + (n - 1) ** 2  
        a.append(neste_verdi)
    return a

# Antall verdier i sekvensen
antall_verdier = 31
sekvens = beregn_sum(antall_verdier)

# Skriv ut resultatet
print("De første 31 tallene i sekvensen er:")
for i, verdi in enumerate(sekvens):
    print(f"a_{i} = {verdi}")
