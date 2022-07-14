n=int(input())
t=n*n
s=0
for i in str(t):
    s+=int(i)
if (s==n):
    print("Neon Number")
else:
    print("Not Neon Number")