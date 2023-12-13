input_1=input()
input_2=input()
input_1=input_1.lower()
input_2=input_2.lower()
count=0
for i in range(len(input_1)):
        if ord(input_1[i]) > ord(input_2[i]): 
              print(1)
              count=1
              break
        elif ord(input_1[i]) > ord(input_2[i]):
              print(-1)
              count=1
              break
if count==0:print(count)