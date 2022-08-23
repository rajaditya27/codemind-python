a,b=map(int,input().split())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
# l=set(l)
# k=set(k)
g=[]
for i in l:
    if i in k and i not in g:
        g.append(i)
print(*g)