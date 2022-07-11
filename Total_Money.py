t=int(input())
for k in range(t):
    D,d,P,Q=map(int,input().split())
    n=D//d
    n2=D%d
    s=0
    
    for i in range(n):
        s+=(P+i*Q)*d
    s+=(P+n*Q)*n2
    print(s)