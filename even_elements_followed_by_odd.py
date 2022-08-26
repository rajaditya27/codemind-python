n=int(input())
l=list(map(int,input().split()))
c=[]
g=[]
for i in l:
    if i%2==0:
        c.append(i)
    else:
        g.append(i)
print(*(c+g))