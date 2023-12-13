k=int(input())
for i in range(k):
    inp=input().split()
    vika="vika"
    vika_count=0
    index=[]
    index_count=0
    for j in range(int(inp[0])):
        name=input().lower()
        for k in range(int(inp[1])):
            if vika_count>3: break
            elif name[k]==vika[vika_count]:
                if len(index)==0:
                    index.append(k)
                    vika_count+=1
                elif k>index[index_count] and index_count<3:
                    index.append(k)
                    index_count+=1
                    vika_count+=1
    if len(index)==4:

        print("YES")
    else: print("NO")            

