T=input()
for l in range(0,int(T)):
    b=int(input())
    c=input()
    c=list(map(int,c.split(" ")))
    if(b%2==0):
        print("no")
    else:
        if(c==c[::-1]):
            a=1
            m=0
            for i in range(int(b/2)):
                if(c[i]==a and c[b-1-i]==a):
                    a=a+1
                else:
                    print("no")
                    m=m+1
                    break
            if(i==int(b/2)-1 and m!=1):
                if(c[int(b/2)]==a):
                    print("yes")
                else:
                    print("no")
        else:
            print("no")
