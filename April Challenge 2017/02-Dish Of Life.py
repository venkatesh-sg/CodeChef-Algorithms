a=input();
for i in range(0,int(a)):
    some=0
    somej=0
    ite=input();
    ite=list(map(int,ite.split(" ")))
    for j in range(0,ite[0]):
        se=input();
        se=list(map(int,se.split(" ")))
        se.pop(0)
        nsim=se if (j==0) else list(set(nsim + se))
        if(len(nsim)==ite[1] and j < ite[0]-1):
            some=1
            somej+=1
            print("some")
            for z in range(j+1,ite[0]):
                dl=input();
            break;
        elif(len(nsim)==ite[1] and j == ite[0]-1):
            print("all")
        elif(len(nsim)!=ite[1] and j == ite[0]-1):
            print("sad")
        
        
    
