inp=input()
arr=[]
for i in inp:
    arr.append(i)
set_it=set(arr)
if len(set_it)%2==0:print("CHAT WITH HER!")
else:print("IGNORE HIM!")