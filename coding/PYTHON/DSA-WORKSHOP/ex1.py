def main():
    # TAKING THE USER DEFINED INPUT
    n = int(input("Enter the number of elements: "))
    a = [int(input(f"Element {i+1}: ")) for i in range(n)]
    # TAKING INPUT FOR INSERTION
    insert = int(input("Enter the index to insert the element (1-based index): ")) -1
    value = int(input("Enter the value to be inserted: "))
    # INSERTING ALGORITHM
    a.insert(insert, value)
    # Display the updated series
    print("The updated series:")
    print(" ".join(map(str, a)))
if __name__ == "__main__":
    main()