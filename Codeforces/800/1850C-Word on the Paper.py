num=int(input())
s=""
for i in range(num):
    for j in range(8):
        inp=input()
        for k in inp:
            if k.isalpha():s+=k
    print(s)
    s=""