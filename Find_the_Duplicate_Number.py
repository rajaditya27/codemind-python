n=int(input())
l=list(map(int,input().split()))[:n]
t=list(map(int,input().split()))[:n]
for i in range(n):
    print(l[i]+t[i],end=' ')