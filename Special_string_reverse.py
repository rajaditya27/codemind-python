s=input()
l=list(s)
a=[]
special=[]
char=[]
for i in range(len(l)):
    if l[i].isalpha():
        a.append(l[i])
    else:
        char.append(l[i])
        special.append(i)
a=a[::-1]
for i in range(len(special)):
    a.insert(special[i],char[i])
print(*a,sep='')