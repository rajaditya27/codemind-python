n=int(input())
l=list(map(int,input().split()))
c=0
m=min(l)
for i in l:
    if len(str(m))==len(str(i)):
        c+=1
print(c)