n=int(input())
l=list(map(int,input().split()))
p=[]
m=[]
for i in l:
    if i%2!=0:
        p.append(i)
    if i%2==0:
        m.append(i)
print(*(p+m))