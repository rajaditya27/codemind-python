a=list(map(int,input().split()))[:3]
b=list(map(int,input().split()))[:3]
c=0
d=0
for i in range(3):
    if a[i]>b[i]:
        c+=1
    if a[i]<b[i]:
        d+=1
print(c,d)