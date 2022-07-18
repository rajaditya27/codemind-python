n=int(input())
l=list(map(int,input().split()))[:n]
l=set(l)
for i in l:
    print(i,end=' ')