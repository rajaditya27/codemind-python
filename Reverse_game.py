def rev(n):
    rev=0
    while(n):
        x=n%10
        rev=rev*10+x
        n=n//10
    return rev
n=int(input())
l=list(map(int,input().split()))
for i in l:
    print(rev(i),end=' ')
    