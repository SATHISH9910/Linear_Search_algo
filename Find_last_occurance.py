arr=[22,33,44,556,6]
target=6
last_index=-1      

for i in range(len(arr)):      # Continues checking the entire array#
    if arr[i]==target:
        last_index=i                                                               #keep updates last index#
if last_index==-1:              #does'nt use break#
    print("element not found")
else:
    print("last occurance is at index",last_index)
                                                                                          