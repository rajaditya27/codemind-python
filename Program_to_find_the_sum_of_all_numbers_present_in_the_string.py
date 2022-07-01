s=input()
sum=0
for i in s:
    if(i.isnumeric()):
        sum=sum+int(i)
print(sum)