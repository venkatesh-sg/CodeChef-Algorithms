T=input()
for i in range(0,int(T)):
    a=input()
    a=list(a)
    b=0
    c=0
    for j in range(0,len(a)):
        if(a[j]=="1" and b==0):
            b=b+1;
        elif(a[j]=="0" and b==1):
            c=c+1;
        elif(a[j]=="1" and c>0):
            b=b+1
        if(b==2):
            break
    if(b==2):
        print("NO")
    elif(b==0 and c==0):
        print("NO")
    else:
        print("YES")
    
        
