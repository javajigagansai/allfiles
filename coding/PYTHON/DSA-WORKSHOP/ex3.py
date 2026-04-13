def main():
    # taking the user-defined input
    n = int(input("Enter the number of elements: "))
    a = [int(input(f"Element {i+1}: ")) for i in range(n)]
    # taking the input for deletion
    insert = int(input("Enter the index of the element to be deleted (1-based index): ")) - 1
    # deletion algorithm
    if 0 <= insert < n:
     for i in range(insert, n - 1):
         a[i] = a[i + 1]
     n -= 1
    # Display the updated array
     print("The updated series:")
     print(" ".join(map(str, a[:n])))
    else:
       print("Invalid index. Please enter a valid index.")
if __name__ == "__main__":
        main()
