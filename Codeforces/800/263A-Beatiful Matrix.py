inp=[""]
for i in range(5):
    inp.append(list(input().split()))
    for j in range(len(inp[i])):
        if inp[i][j]=="1":
            location_y=i+1
            location_x=j+1
print(abs(location_y-3)+abs(location_x-3))