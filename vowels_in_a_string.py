n=input()
a=input()
for i in range(len(n)):
    if a in n[i]:
        print(True)
        print(i)
        break
else:
    print(False)