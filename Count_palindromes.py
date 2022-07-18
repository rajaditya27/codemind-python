def rev(n):
    rev=0
    while(n):
        x=n%10
        rev=rev*10+x
        n=n//10
    return rev
n=int(input())
l=list(map(int,input().split()))

c=0
for i in l:
    if rev(i)==i:
        c+=1
print(c)