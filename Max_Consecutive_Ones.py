n=int(input())
l=list(map(int,input().split()))
r=0
c=0
for i in l:
      if i==0:
          c=0
      else:
        c+=1
        r=max(r,c)
print(r)