n = 5
stack = []
top = 0
j = 1
print("Stack using list:")
print("-------------------------------------------------------------------")
while True:
    print("\n1. Insertion\n2. Deletion\n3. Display\n4. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        if top >= n:
            print("The stack is full.")
        else:
            value = int(input(f"Enter value {j}: "))
            stack.append(value)
            top += 1
            j += 1
    elif ch == 2:
        if top == 0:
            print("Stack is empty.")
        else:
            deleted = stack.pop()
            print(f"The deleted element is {deleted}")
            top -= 1
    elif ch == 3:
        if top == 0:
            print("No elements in stack to be shown.")
        else:
            print("The stack elements are:")
            for i in range(top-1, -1, -1):
                print(stack[i])
    elif ch == 4:
        print("Exit")
        break
    else:
        print("Invalid option")