n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n+1):
    if i==n-1:
        break
    if l[i]<l[i+1]:
        c+=1
if c==n-1:
    print('yes')
else:
    print('no')