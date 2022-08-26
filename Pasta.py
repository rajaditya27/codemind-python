a,b=map(int,input().split())
c=0
l=list(map(int,input().split()))
m=list(map(int,input().split()))
for i in m:
    if i in l:
        l.remove(i)
    else:
        c=1
        break
if c==0:
    print('Yes')
else:
    print('No')