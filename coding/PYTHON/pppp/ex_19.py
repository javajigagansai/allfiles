#to sort the list
print("enter the elements in the list by giveing spaces")
g=list(map(int, input("Enter numbers separated by spaces: ").split()))
print("list",g)
print("the sorted list:",sorted(g))