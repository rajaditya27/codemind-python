n=int(input())
l=list(map(int,input().split()))
z=int(input())
c=0
for i in range(n):
    if l[i]==z:
        c+=1
# else:
    # print(0)
print(c)