n=int(input())
c=0
while(n):
    n-=1
    a=int(input())
    l=list(map(int,input().split()))[:a]
    c=0
    for i in l:
        if i%2!=0:
            c+=1
    print(c//2)