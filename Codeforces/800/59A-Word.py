s=input()
upper_count=0
lower_count=0
for i in range(len(s)):
    if ord(s[i])<97: upper_count+=1
    else: lower_count+=1
if upper_count>lower_count: print(s.upper())
else:print(s.lower())
