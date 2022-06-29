n=int(input())
import math    
p=math.sqrt(n)
x=math.floor(p)
if x-p==0:
    print('True')
else:
    print('False')