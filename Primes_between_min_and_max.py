def prime(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    for i in range(2,int(n**0.5)+2):
        if n%i==0:
            return 0
    return 1
n=int(input())
a=list(map(int,input().split()))
c=0
# for i in a:
ma = a.index(max(a))
mi = a.index(min(a))
# c = 0
if mi<ma:
    for i in range(mi,ma+1):
        if prime(a[i]):
            c+=1
    print(c)
else:
    for i in range(ma,mi+1):
        if prime(a[i]):
            c+=1
    print(c)