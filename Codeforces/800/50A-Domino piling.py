size=input().split()
size_multip=int(size[0])*int(size[1])
if(size_multip%2==0): print(int(size_multip/2))
else: print(int((size_multip-1)/2))