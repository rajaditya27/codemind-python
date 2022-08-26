n=int(input())
l=list(map(int,input().split()))
avg=sum(l)//n
for i in l:
    if avg==i:
        print(True)
        break
else:
    print(False)