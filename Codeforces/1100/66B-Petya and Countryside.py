n=int(input())
arr=input().split()
count_of_each=[]
for i in range(n):
    count=1
    if i!=0:
        j=i-1
        c=i
        while(j>=0):
            if int(arr[c])>=int(arr[j]):
                count+=1
                max=int(arr[j])
                j-=1
            else:break
            c-=1
    c=i
    for k in range(i+1,n):
        if int(arr[c])>=int(arr[k]):
            count+=1
            max=int(arr[k])
        else:break
        c+=1
    count_of_each.append(count)
count_of_each.sort()
print(count_of_each[-1])
