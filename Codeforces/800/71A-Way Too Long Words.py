k=input()
k=int(k)
for i in range(k):
    inp=input()
    if len(inp)<=10:
        print(inp)
    else:
        print(inp[0]+"{}".format(len(inp[1:])-1)+inp[-1])
3