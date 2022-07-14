def add(n):
    s=0
    while(n):
        x=n%10
        s+=x
        n=n//10
    return s

def multiply(n):
    m=1
    while(n):
        t=n%10
        m*=t
        n=n//10
    return m

n=int(input())
if n>10:
    p=multiply(n)
    l=add(n)
    print(p-l)