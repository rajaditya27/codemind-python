a,b=map(int,input().split())
n=list(map(int,input().split()))
m=list(map(int,input().split()))
# n=set(n)
# m=set(m)
c=[]
# g=[]
for i in n:
    if i in m and i not in c:
        c.append(i)
# for i in m:
#     if i in n:
#         c.append(i)
print(*c)