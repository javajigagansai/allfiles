class Node:
    def __init__(self, data):  # ✅ Fixed: __init__ (double underscores)
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):  # ✅ Fixed: __init__ (double underscores)
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Create a linked list
my_list = LinkedList()

# Add elements to the linked list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Display the elements of the linked list
print("Elements of the linked list:")
my_list.display()
