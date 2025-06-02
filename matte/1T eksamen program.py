n = 1
sum = 4

def a(n):
    return n**2+2*n+1

while sum < 1000000:
    sum += a(n+1)
    n += 1

print(n, a(n), sum-a(n))
