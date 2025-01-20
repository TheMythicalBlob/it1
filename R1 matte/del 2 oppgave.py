def f(n):
    if n== 1:
        return 1
    else: 
        return 2*f(n-1)+1
    
for i in range(1,10):
    print(f(i))