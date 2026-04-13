def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
arr = [1, 3, 4, 5, 9, 13]
result = binary_search(arr, 13)
if result != -1:
    print(f"Target found at index: {result}")
else:
    print("Target not found.")