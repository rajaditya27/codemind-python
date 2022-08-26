s=input().lower()
g=[]
for i in s:
    if s.count(i)==1 and i!=' ':
        g.append(i)
        g.sort()
for i in g:
    print(i,end='')