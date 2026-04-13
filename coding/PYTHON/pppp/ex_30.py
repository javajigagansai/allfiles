def linear_search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1
numbers = [int(x) for x in input("Enter numbers: ").split()]
target = int(input("Enter the number to search for: "))
result = linear_search(numbers, target)
if result != -1:
    print(f"Number found at index {result}")
else:
    print("Number not found")
