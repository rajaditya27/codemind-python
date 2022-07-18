def rev(n):
    rev=0
    while(n):
        x=n%10
        rev+=x
        n=n//10
    return rev
n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    s+=rev(i)
print(s)