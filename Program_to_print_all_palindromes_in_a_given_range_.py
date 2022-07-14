def rev(n):
    s=0
    while(n):
        r=n%10
        s=s*10+r
        n=n//10
    return s

m=int(input())
n=int(input())
# p=rev(n)
for i in range(m,n+1):
    p=rev(i)
    if i==p:
        print(i,end=" ")