a = input();
for i in range(0,int(a)):
    b=input()
    b=list(map(int,b.split(" ")))
    c=list(input())
    l = [[None]] * b[1]
    for i in range(0,b[1]):
        l[i]=list(input())
    xo=[]    
    for j in range(0,b[1]):
        for k in range(0,b[1]):
            x=j
            y=k
            z=0
            while (x!=-1 and y!=-1 and z!=len(c)+1 and x!=b[1] and y!=b[1] and l[x][y]!="#"):
                if(z==len(c)):
                    z=z+1
                    break
                if(c[z]=="R"):
                    y+=1
                if(c[z]=="L"):
                    y-=1
                if(c[z]=="U"):
                    x-=1
                if(c[z]=="D"):
                    x+=1
                z+=1
            if(z>1):
                xo.append(z-1)
    
    xr=xo[0]
    for v in range(1,len(xo)):
        xr=xr^xo[v]
    print(xr)
            
        
    
