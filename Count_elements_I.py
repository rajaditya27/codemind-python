a,b=map(int,input().split())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
l=set(l)
k=set(k)
g=[]
for i in l:
    if i in k:
        g.append(i)
# for i in k:
#     if i in l:
#         g.append(i)
print(len(g))