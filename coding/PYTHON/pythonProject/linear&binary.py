def linear_search(arr,search):
    for i in range(len(arr)):
        if arr[i]==search:
            return i
    return -1
arr=[23,5,4,3,9]
result = linear_search(arr, 3)
if result!=-1:
    print(f"element found at position {result}")
else:
    print(f"element not found")