n=int(input())
l=list(map(int,input().split()))
for i in l:
    m=len(str(i))
    if i<0:
        m-=1
    print(m,end=' ')