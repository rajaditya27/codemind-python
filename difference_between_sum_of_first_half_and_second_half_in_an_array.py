n=int(input())
l=list(map(int,input().split()))
c=(l[:n//2])
k=(l[n//2:])
a=sum(c)
b=sum(k)
print(abs(a-b))