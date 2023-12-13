k=int(input())
for i in range(k):
    n=int(input())
    inp=input().split()
    b=[]
    c=[]
    for v in range(len(inp)):
        inp[v]=int(inp[v])
    inp.sort()
    maximum=max(inp)
    s=len(inp)-1
    for j in inp:
        b.append(j)
    while(maximum in b):
        c.append(inp[s])
        s-=1
        b.remove(maximum)
    if len(b)==0: print(-1)
    else:
        print("{} {}".format(len(b),len(c)))
        for t in b:
            print(t, end=" ")
        print("")
        for t in c:
            print(t,end=" ")
        print("")
