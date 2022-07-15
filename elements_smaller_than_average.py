n=int(input())
l=list(map(int,input().split()))
a=sum(l)
p=a//n
h=0
for i in range(n):
    if(l[i]<=p):
        h+=1
print(h)