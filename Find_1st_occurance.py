arr=[23,45,67,34,2]
target=23
found=False           # i =index

for i in range(len(arr)):      # loop through all indices[all elements returns]
    if arr[i]==target:       # compare the value not the index
        print("First occurance at index",i)
        found=True
        break
if not found:            # runs only if no match was found
    print("Element not Found")


    arr=[23,45,67,34,2]
target=23
found=False           # i =index

for i in range(len(arr)-1):      # loop through all indices[all elements returns]
    if arr[i]==target:       # compare the value not the index
        print("First occurance at index",i)
        found=True
        break
if not found:            # runs only if no match was found
    print("Element not Found")