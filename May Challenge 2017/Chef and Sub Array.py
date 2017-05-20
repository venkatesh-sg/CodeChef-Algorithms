def shift(l, n):
    return l[len(l)-n:] + l[:len(l)-n]
a=input()
a=list(map(int,a.split(" ")))
b=input()
N=a[0]
K=a[1]
P=a[2]
s=0
B=[0]*(N-K+1)
b=list(map(int,b.split(" ")))
for i in range(0,N-K+1):
    B[i]=sum(b[i:i+K])
c=list(input())
for i in range(0,P):
    if(c[i]=="!"):
        s=s+1
    if(c[i]=="?"):
        b=shift(b,s)
        B=shift(B,s)
        for y in range(0,s):
            B[y]=sum(b[y:y+K])
        max_s=max(B)
        print(max_s)
        s=0
        
