T=input()
for i in range(0,int(T)):
    n=input()
    a=input()
    a=list(map(int,a.split(" ")))
    max_p=max(a)
    courses=int(n)-max_p
    print(courses)
