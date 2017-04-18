a = input();
for i in range(0,int(a)):
    seq=input();
    seq=list(seq)
    while len(seq)!=0:
        if(seq[0]=="0"):
            seq.pop(0)
        elif(seq[len(seq)-1]=="1"):
            seq.pop(len(seq)-1)
        else:
            break
    if(len(seq)==0):
        print("0")
        continue
    nz=0
    nou=1
    sum=0
    for k in range(len(seq),0,-1):
        if(seq[k-1]=="0"):
                nz+=1
        else:
            sum=sum+nz+nou
            if(seq[k-2]=="0"):
                nou+=1
    print(sum)
    
        
        
