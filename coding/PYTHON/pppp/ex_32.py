def sorting_numbers_by_insertion(numbers):
    return sorted(numbers)
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
sorted_numbers =  sorting_numbers_by_insertion(numbers)
print("Sorted numbers:", sorted_numbers)