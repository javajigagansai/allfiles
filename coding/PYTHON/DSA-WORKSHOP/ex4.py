def main():
    # Input the number of elements
    n = int(input("Enter the number of elements: "))
    a = []
    # Input the elements of the array
    for i in range(n):
        element = int(input(f"Element {i + 1}: "))
        a.append(element)
    # Input the element to be searched
    s = int(input("Enter the element to be searched: "))
    # Linear search for the element
    found_index = -1 # Initialize found_index to -1 (not found)
    for i in range(n):
        if s == a[i]:
            found_index = i # Update found_index with the current index
            break
    # Display the result
    if found_index != -1:
        print(f"Element found at index {found_index+1}.") # Output index if found
    else:
        print("Element not found.")
if __name__ == "__main__":
    main()