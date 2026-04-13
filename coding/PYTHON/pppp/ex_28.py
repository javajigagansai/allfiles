def sort_numbers(numbers):
    return sorted(numbers)
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
sorted_numbers = sort_numbers(numbers)
print("Sorted numbers:", sorted_numbers)