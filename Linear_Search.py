arr=[22,234,4,56546,7]
target=4
Found=False

for num in arr:
    if num == target:
        Found= True
        break

if Found:
    print("Element Found");
else:
    print("Element not Found")


# Time Complexity: O(n)
# Space Complexity: O(1)

arr=[10,20,30,40,50]
Target=40

Found=False
for i in range(len(arr)):
    if arr[i] == Target:
        print("Element Found at index", i)
        Found=True

if not Found:
    print("Element not found")