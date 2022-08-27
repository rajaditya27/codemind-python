n=int(input())
l=list(map(int,input().split()))
k=int(input())
c=[]
for i in l:
    if i<=k:
        c.append(i)
    # else:
    #     break
print(sum(c))