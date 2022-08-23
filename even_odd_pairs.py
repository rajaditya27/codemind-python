n=int(input())
l=list(map(int,input().split()))
c=[]
k=[]
for i in range(n):
    if l[i]%2==0:
        c.append(l[i])
    else:
        k.append(l[i])
i=0
j=0
while i<len(c) or j<len(k):
    if i<len(c):
        print(c[i],end=' ')
        i+=1
    if j<len(k):
        print(k[j],end=' ')
        j+=1
if n%2!=0:
    print(0)