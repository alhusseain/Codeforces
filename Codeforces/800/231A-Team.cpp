k=int(input())
count=0
for i in range(k):
    inp=input().split()
    a=int(inp[0])
    b=int(inp[1])
    c=int(inp[2])
    if (a==1 and b==1) or (a==1 and c==1) or (b==1 and c==1): count+=1
print(count)