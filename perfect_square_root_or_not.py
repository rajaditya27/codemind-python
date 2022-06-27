import math 
n=int(input())
x=math.sqrt(n)
y=(x-math.floor(x))
if(y==0):
    print('True')
else:
    print('False')