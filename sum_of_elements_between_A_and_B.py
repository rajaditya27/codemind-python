n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
for i in range(len(l)):
    if (a<=l[i] and b>=l[i]):
        c.append(l[i])
print(sum(c))
# else:
    # print(-1)