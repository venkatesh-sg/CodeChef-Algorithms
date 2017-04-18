T=input()
for i in range(0,int(T)):
    b=input()
    b=list(map(int,b.split(" ")))
    ll=[]
    for j in range(0,b[0]):
        new=[float("inf")]*b[0]
        for k in range(0,b[1]):
            if(j<b[1]):
                new[k]=b[2]
        ll.append(new)
    for x in range(0,b[0]):
        ll[x][x]=0
    for j in range(0,b[3]):
        c=input()
        c=list(map(int,c.split(" ")))
        ll[c[0]-1][c[1]-1]=c[2]
        ll[c[1]-1][c[0]-1]=c[2]
    n=b[0]
    for m in range(0,n):
            for j in range(m,n):
                for k in range(0,n):
                    ll[m][j] = min(ll[m][j], ll[m][k] + ll[k][j])
                    ll[j][m]=ll[m][j]
    print(*ll[b[4]-1], sep=' ')
