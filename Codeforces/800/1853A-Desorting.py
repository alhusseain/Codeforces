k=int(input())
for i in range(k):
    n=input()
    n=int(n)
    diff=[]
    inp=input().split()
    for i in range(len(inp)):
        if i!=len(inp)-1:
            diff.append(int(inp[i+1])-int(inp[i]))
    diff.sort()
    if diff[0]<0: print(0)
    elif diff[0]==0 or diff[0]==1: print(1)
    else:
        if diff[0]%2!=0: diff[0]=diff[0]-1
        print(int((diff[0]+2)/2))
    
