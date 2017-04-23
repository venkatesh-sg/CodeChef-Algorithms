T=input()
for i in range(0,int(T)):
    a=input()
    a=list(map(int,a.split(" ")))
    A=0
    B=0
    w=""
    for i in range(1,a[0]+a[1]+10):
        if(i%2==0):
            B=B+i;
            if(B>a[1]):
                w="Limak"
                break
        if(i%2!=0):
            A=A+i
            if(A>a[0]):
                w="Bob"
                break
    print(w)
