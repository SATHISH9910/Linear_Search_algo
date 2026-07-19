arr=[10,30,20,10,20,30,20,]
target=20
count=0

for num in arr:
    if num == target:
        count+=1
print("Target appears", count)

# Time Complexity: O(n)
# Space Complexity: O(1)