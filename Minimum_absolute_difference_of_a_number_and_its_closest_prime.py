k=int(input())
for i in range(k,2,-1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        break
for m in range(k+1,k+100):
    for n in range(2,m):
        if m%n==0:
            break
    else:
        break
if abs(k-m)>=abs(k-i):
    print(abs(k-i))
else:
    print(abs(k-m))