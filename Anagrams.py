s1=input().lower()
s2=input().lower()

for i in s1:
    if i not in s2:
        print(False)
        break
else:
    print(True)