n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in l:
    p=len(str(i))
    if i<0:
        p-=1
    if p==k:
        c+=1
print(c)