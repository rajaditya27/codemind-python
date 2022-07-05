n=int(input())
c=0
arr=list(map(int,input().split()))
for i in range (n):
    if i==0 or i==n-1:
        continue
    elif arr[i+1]%2==0 and arr[i-1]%2!=0 or arr[i+1]%2!=0 and arr[i-1]%2==0:
        c+=1
print(c)