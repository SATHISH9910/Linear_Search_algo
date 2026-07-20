arr=[22,33,22,3343,4545,22]
target=22
found=False

for i in range(len(arr)):
    if arr[i]==target:
        print('Element found at index',i)
        found=True
if not found:
    print("Element not found")