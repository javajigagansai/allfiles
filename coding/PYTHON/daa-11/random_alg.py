import random

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

# Example usage
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = randomized_quick_sort(arr)
print("Sorted array:", sorted_arr)
