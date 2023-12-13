k=int(input())
for i in range(k):
    names=[]
    vika="vika"
    vika_count=0
    found=[]
    inp=input().split()
    for j in range(int(inp[0])):
        names.append(input())
    for j in range(int(inp[1])):
        exist=False
        for k in range(int(inp[0])):
            if vika_count>3:break
            elif names[k][j]==vika[vika_count]:
                found.append(names[k][j])
                exist=True
                break
        if exist:vika_count+=1
    if len(found)==4: print("YES")
    else:print("NO")