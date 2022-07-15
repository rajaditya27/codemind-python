def palindrome(n):
    rev=0
    temp=n
    while(n>0):
        x=n%10
        rev=rev*10+x
        n=n//10
    if temp==rev:
        return True
    else:
        return False
# t=int(input())
# for k in range(t):
n=int(input())
print(palindrome(n))