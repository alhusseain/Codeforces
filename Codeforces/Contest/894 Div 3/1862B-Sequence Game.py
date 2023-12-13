k=int(input())
for i in range(k):
    n=int(input())
    seq=input().split()
    arr=[seq[0]]
    for j in range(1,len(seq)):
        if int(seq[j])<int(seq[j-1]):
            arr.append("1")
            arr.append(seq[j])
        else:
            arr.append(seq[j])
    print(len(arr))
    print(" ".join(arr))

