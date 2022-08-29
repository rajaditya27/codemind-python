s=input().lower().split()
l1=list(s[0])
s.remove(s[0])
c=0
e=[]
for i in l1:
    for j in range(len(s)):
        if i not in s[j] and i not in e:
            break
    else:
        e.append(i)
print(len(e))