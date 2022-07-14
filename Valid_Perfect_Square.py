t=int(input())
for k in range(t):
    n=int(input())
    for i in range (n+1):
        if i**2==n:
            print("True")
            break
    else:
        print("False")