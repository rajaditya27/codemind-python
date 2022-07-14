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
for i in range (n):
    p=add(n)
    l=multiply(n)
    if(p==l):
        print('Spy Number')
        break
else:
    print('Not Spy Number')