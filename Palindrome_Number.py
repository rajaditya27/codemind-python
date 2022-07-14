def palindrome(n):
    s=0
    temp=n
    while(n>0):
        s=s*10+n%10
        n=n//10
    if temp==s:
           return True
    else:
           return False 
t= int(input())
for k in range (t):
      n=int(input())
      print(palindrome(n))