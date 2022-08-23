def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**.5)+1):
        if n%i==0:
            return False
    return True
    
n=int(input())
l=list(map(int,input().split()))
c=0
ma=l.index(max(l))
mi=l.index(min(l))
if mi<ma:
    for i in range(mi,ma+1):
        if prime(l[i]):
            c+=1
    print(c)
else:
    for i in range(ma,mi+1):
        if prime(l[i]):
            c+=1
    print(c)

