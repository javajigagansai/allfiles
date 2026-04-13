def binary_search(arr, target):
    x = 0
    z = len(arr) - 1
    while x <= z:
        y = (x + z) // 2 # Use integer division to find the mid-point
        if target == arr[y]:
            return y # Element found
        elif target > arr[y]:
            x = y + 1 # Search in the right half
        else:
         z = y - 1 # Search in the left half
    return -1 # Element not found
def main():
    n = int(input("Enter the number of elements: "))
    a = []
    # Input the elements of the array
    for i in range(n):
        element = int(input(f"Element {i + 1}: "))
        a.append(element)
    # Sort the array for binary search
    a.sort()
    # Input the element to be searched
    s = int(input("Enter the element to be searched: "))
    # Perform binary search
    index = binary_search(a, s)
    # Display the result
    if index != -1:
        print(f"Element found at index {index} (0-based index).")
    else:
        print("Element not found.")
if __name__ == "__main__":
    main()