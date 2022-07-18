a=int(input())
l=list(map(int,input().split()))[:a]
c=int(input())
if c in l:
    print(l.index(c))
else:
    print(-1)