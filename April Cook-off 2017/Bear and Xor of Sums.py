N=input()
a=input()
a=list(map(int,a.split(" ")))
b=[]
for j in range (0,len(a)):
    for i in range(j,len(a)):
        segsum=0
        for l in range(j,i+1):
            segsum=segsum+a[l]
        b.append(segsum)
xor=b[0]
for k in range(1,len(b)):
    xor=xor^b[k]
print(xor)
    
