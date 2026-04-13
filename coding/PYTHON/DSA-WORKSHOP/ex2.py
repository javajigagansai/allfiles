def main():
    # taking the user-defined array
    n = int(input("Enter the number of elements: "))
    a = [int(input(f"Element {i+1}: ")) for i in range(n)]
    # taking input for replacement
    insert = int(input("Enter the index of the element to be replaced (1-based index): ")) - 1
    value = int(input("Enter the value to be replaced: "))
    # replacing
    a[insert] = value
    # Display the updated array
    print("The updated series:")
    print(" ".join(map(str, a)))
if __name__ == "__main__":
    main()