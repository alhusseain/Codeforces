inp=input().split()
sum=0
for i in range(1,int(inp[2])+1):
    sum+=i*int(inp[0])
borrow=sum-int(inp[1])
if borrow<0:print(0)
else: print(borrow)