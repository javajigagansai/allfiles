def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid  # Return index of target element

    return -1  # Return -1 if target is not in the list


# Get input from the user and sort the list
arr = list(map(int, input("Enter elements of the sorted list separated by space: ").split()))
target = int(input("Enter the target element to search for: "))
result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")
