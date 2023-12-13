k=int(input())
inp=input()
count=0
for i in range(len(inp)):
    if i!=len(inp)-1:
        if inp[i]==inp[i+1]: count+=1
print(count)
