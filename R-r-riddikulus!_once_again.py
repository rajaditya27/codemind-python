a,b=map(int,input().split())
l=list(map(int,input().split()))
t=a-b
while(t):
    t-=1
    k=l.pop()
    l.insert(0,k)
print(*l)