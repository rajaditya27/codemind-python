a=int(input())
t=a
a=abs(a)
r=0
while(a):
    d=a%10
    r=r*10+d
    a//=10
if(t<0):
    print('-%d'%r)
else:
    print(r)