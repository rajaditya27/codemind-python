n=int(input())
m=int(input())
k=0
for i in  range(n):
    a=[]
    a=list(map(int,input().split()))[:m]
    k+=sum(a)
print(k)