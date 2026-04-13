def binary_search(numbers, searched):
    start = 0
    peek = len(numbers) - 1
    while start <= peek:
        mean = (start + peek) // 2
        if numbers[mean] == searched:
            return mean
        elif numbers[mean] < searched:
            peek = mean + 1
        else:
            peek = mean - 1
    return -1
numbers = sorted([int(x) for x in input("Enter sorted numbers: ").split()])
searched = int(input("Enter the number to search for: "))
result = binary_search(numbers, searched)
if result != -1:
    print(f"Number found at index {result}")
else:
    print("Number not found")
