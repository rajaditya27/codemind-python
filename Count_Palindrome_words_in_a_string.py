s=input().lower().split()
c=0
for i in s:
    n=str(i)
    if n==n[::-1]:
        c+=1
print(c)