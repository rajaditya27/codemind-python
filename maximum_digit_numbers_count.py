def lenj(s):
    if s<0:
        s-1*s
    return len(str(s))

n=int(input())
l=list(map(int,input().split()))
k=[]

for i in l:
    k.append(lenj(i))
p=max(k)
for i in l:
    if lenj(i)==p:
        print(i,end=' ')
# print(c)