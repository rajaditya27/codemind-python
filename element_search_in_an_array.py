n=int(input())
arr=list(map(int,input().strip().split()))[:n]
m=int(input())
flag=0
for i in range(n):
    if arr[i]==m:
        flag=1
        break
if flag==1:
    print('True')
else:
    print('False')