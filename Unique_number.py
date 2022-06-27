n=int(input())
a=len(str(n))
p=len(set(str(n)))
if a==p:
    print('Unique Number')
else:
    print('Not Unique Number')