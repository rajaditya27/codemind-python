n=int(input())
l=list(map(int,input().split()))
z=int(input())
for i in l:
    if i==z:
        print(True)
        break
else:
    print(False)