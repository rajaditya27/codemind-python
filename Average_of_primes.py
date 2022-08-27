def prime(n):
    if n==1:
        return False
    elif n==2:
        return True
    for i in range(2,int(n**0.5)+2):
        if n%i==0:
            return False
    return True
n=int(input())
a=list(map(int,input().split()))
s=0
c=0
for i in a:
    if prime(i):
        s+=i
        c+=1
m=s/c
print('%.2f'%m)