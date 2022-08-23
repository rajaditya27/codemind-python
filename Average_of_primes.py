def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**.5)+1):
        if n%i==0:
            return False
    else:
        return True
        
n=int(input())
s=0
count=0
l=list(map(int,input().split()))
for i in l:
    if prime(i):
        s+=i
        count+=1
avg=s/count
print('%.2f'%avg)