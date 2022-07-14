def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0
        
m=int(input())
n=int(input())
for i in range (m,n+1):
    if prime(i):
        print(i)