s=list(input().split())
mn,mx=0,0
# l=list(s.split(" "))
for i in s:
    mn=ord(min(i))
    mx=ord(max(i))
    print(abs(mx-mn),end=" ")