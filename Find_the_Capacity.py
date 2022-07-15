x,y,z=map(int,input().split())
t=2*x*y*z*512
k=t//1024
print(k,end='KB')