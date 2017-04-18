a = input();
for i in range(0,int(a)):
    dish1=input()
    dish2=input()
    ld1=dish1.split(" ")
    ld2=dish2.split(" ")
    sim =set(ld1) & set(ld2)
    if(len(sim)>1):
        print("similar")
    else:
        print("dissimilar")
        
