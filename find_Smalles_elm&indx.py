arr=[24,44,53,22,4,5]
smallest=arr[0]
smallest_index=0

for i in range(len(arr)):
    if arr[i]<smallest:
        smallest=arr[i]
        samllest_index=i

print("Smallest element is",smallest)
print("Index of Smallest element is",samllest_index)