k=input().split()
inp=input().split()
count=0
if int(k[0])==1 or int(k[0])==0:print(0)
elif int(inp[int(k[1])])==int(inp[int(k[1])-1]) and int(inp[int(k[1])])!=0:print(int(k[1])+1)
elif int(inp[int(k[1])])>int(inp[int(k[1])-1]) and int(inp[int(k[1])])!=0:print(int(k[1]))
else:print(0)
