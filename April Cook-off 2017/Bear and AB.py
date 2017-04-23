T=input()
for i in range(0,int(T)):
    a=input()
    a=list(map(int,a.split(" ")))
    s=input()
    c=0
    bc=0
    for j in range(0,len(s)):
        if(s[j]=='a'):
            for l in range(j,len(s)):
                if(s[l]=='b'):
                    c=c+1
        elif(s[j]=='b'):
            for l in range(j,len(s)):
                if(s[l]=='a'):
                    bc=bc+1
    b=c*a[1]*(a[1]+1)
    b1=bc*a[1]*(a[1]-1)
    print ((b+b1)//2)
