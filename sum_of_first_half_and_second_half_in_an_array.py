n=int(input())
l=list(map(int,input().split()))
c=[]
g=[]
for i in range(n):
    if l[i]<=n/2:
        c.append(l[i])
    else:
        g.append(l[i])
print(sum(c))
print(sum(g))
 

    