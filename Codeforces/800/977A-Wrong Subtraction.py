inp=input().split()
count=int(inp[1])
while(count):
    if inp[0][-1]!="0":inp[0]=str(int(inp[0])-1)
    else:
        inp[0]=str(int(inp[0])//10)
    count-=1
print(inp[0])