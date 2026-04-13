#to print the decending order of the list
print("enter the elements in the list by giving spaces")
g=list(map(int, input("Enter numbers separated by spaces: ").split()))
print("list",g)
g.sort()
g.reverse()
print("the decending list:",g)
