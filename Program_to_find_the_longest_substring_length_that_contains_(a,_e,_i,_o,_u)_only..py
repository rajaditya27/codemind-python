count=0
a=input()
for i in range (0,len(a)):
    if a[i] in 'aeiou':
        c=1
        for j in range (i+1,len(a)):
            if a[j] in 'aeiou':
                c+=1
            else:
                break
        if c>count:
            count=c
print(count)