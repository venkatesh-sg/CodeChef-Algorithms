a=input()
for i in range(0,int(a)):
    b=input()
    b=b.split(" ")
    c=input()
    c=list(map(int,c.split(" ")))
    for j in range(0,int(b[1])):
        d=input()
        d=list(map(int,d.split(" ")))
        oda=0
        od=0
        for k in range(d[0]-1,d[1]-1):
            if(c[k]==c[k+1]):
                od+=1
            else:
                od=0
            if(od==d[2]-1):
                oda+=1
        if(d[2]==1):
            oda+=1
        print(oda)
    
