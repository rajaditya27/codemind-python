n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    if l.count(i)==i and i not in c:
        c.append(i)
if len(c)==0:
    print(-1)
else:
    print(*c)
   
   
   