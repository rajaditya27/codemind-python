n=int(input())
l=list(map(int,input().split()))
l=set(l)
c=[]
for i in l:
    if i%2!=0:
        c.append(i)
print(sum(c))