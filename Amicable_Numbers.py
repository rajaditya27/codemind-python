a=int(input())
b=int(input())
sum=0
sum1=0
for i in range (1,int(a/2)+1):
    if a%i==0:
        sum+=i
for i in range (1,int(b/2)+1):
    if b%i==0:
        sum1+=i
        
if(sum==b and sum1==a):
    print('Amicable')
else:
    print('Not Amicable')