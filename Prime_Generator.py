def prime(n):
    if n<2:
        return 0
    if n==2:
        return 1
    if n&1==0:
        return 0
    i = 3 
    while i*i<=n:
        if n%i==0:
            return 0
        i += 2    
    return 1



for _ in range(int(input())):
    a,b = tuple(map(int,input().split()))
    for i in range(a,b+1):
        if prime(i):
            print(i)
    print()