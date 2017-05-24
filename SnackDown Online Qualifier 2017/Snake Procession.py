T=input()
for i in range(0,int(T)):
    b=input()
    c=str(input())
    c=c.replace('.','')
    if(len(c)%2!=0):
        print("Invalid")
    else:
        for i in range(0,len(c)):
            if(i%2==0):
                if(c[i]!="H"):
                    print("Invalid")
                    break
            else:
                if(c[i]!="T"):
                    print("Invalid")
                    break

    if(i==len(c)-1 or len(c)==0):
        print("Valid")
