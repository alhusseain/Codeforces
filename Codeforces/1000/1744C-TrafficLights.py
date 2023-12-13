k=int(input())
for i in range(k): 
    input_arr=input().split()
    arr=input()
    arr+=arr
    #index_key=[]
    index_length=[]
    counting=False
    count=0
    #arg_count=0
    arr_size=int(input_arr[0])
    if input_arr[1]=="g": print(0)
    else:
        # for letter in arr :
        #     if letter==input_arr[1]:arg_count=arg_count+1
        j=0
        for j in range(len(arr)):
            if(arr[j]==input_arr[1] and counting==False):
                chosen_one=j
                counting=True
                # index_key.append(chosen_one)
            
            # if(counting==True ):count+=1
            if(arr[j]=="g" and counting==True):
                index_length.append(j-chosen_one)
                counting=False
                # count=0
            
            j+=1
        print(sorted(index_length)[-1])
            
        


