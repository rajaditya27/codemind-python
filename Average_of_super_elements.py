n=int(input())
l=list(map(int,input().split()))
s=0
c=[]
for i in l:
    if l.count(i)==i and i not in c:
        s+=i
        c.append(i)
if len(c)==0:
    print(-1)
else:
    avg=s/len(c)
    print('%.2f'%avg)