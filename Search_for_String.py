names=["sathish","Adesh","Vignesh","Shannu"]
target="Shannu"
found=False

for i in range(len(names)):
    if names[i] == target:
        print("Element is found at index",i)
        found=True
        break

if not found:
    print("Element is not found")