n=int(input())
c=0
while(n>=0):
    v=input()
    c=0
    for i in v:
        if(i.isdigit()):
            c+=1
    if(c==len(v)):
        print(True)
    else:
        print(False)