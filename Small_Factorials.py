t=int(input())
while t:
    t-=1
    n=int(input())
    fact=1
    while n!=1:
        fact=fact*n
        n-=1
    print(fact)