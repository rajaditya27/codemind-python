s=input()
s=s.split()
c=[]
for i in s:
    # print(len(s))
    c.append(len(i))
print(min(c))