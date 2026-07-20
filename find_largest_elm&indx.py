arr=[343,435,67,68678]

largest=arr[0]
larges_index= 0

for i in range(len(arr)):
    if arr[i] > largest:
        largest= arr[i]
        larges_index= i
print("Largest element is", largest)
print("Index of largest element is",larges_index)
