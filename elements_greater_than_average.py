n=int(input())
l=list(map(int,input().split()))
c=0
avg=sum(l)//n
for i in l:
    if i>=avg:
        c+=1
print(c)