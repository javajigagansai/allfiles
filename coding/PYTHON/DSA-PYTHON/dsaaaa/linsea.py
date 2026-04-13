def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
arr = list(map(int, input("Enter elements of the list separated by space: ").split()))
target = int(input("Enter the target element to search for: "))
result = linear_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")
