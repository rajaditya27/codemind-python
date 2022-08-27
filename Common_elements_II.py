a,b=map(int,input().split())
n=list(map(int,input().split()))
m=list(map(int,input().split()))
c=[]
g=[]
for i in n:
    if i not in m:
        c.append(i)
for i in m:
    if i not in n:
        g.append(i)
print(*(c+g))