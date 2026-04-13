class Node:#single ll
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    def insert_at_middle(self, value, position):
        if position <= 0:
            print("Invalid position")
            return
        new_node = Node(value)
        if position == 1:
            self.insert_at_beginning(value)
        else:
            current = self.head
            count = 1
            while current and count < position - 1:
                count += 1
                current = current.next
            if current is None:
                print(f"Position {position} is out of bounds")
            else:
                new_node.next = current.next
                current.next = new_node
    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def delete_node_beg(self, value):#single-ll
        current = self.head
        if current.value == value:
            self.head = current.next
        else:
            while current.next:
                if current.next.value == value:
                    current.next = current.next.next
                    break
                current = current.next
    def delete_at_middle(self, position):
        if self.head is None:
            print("List is empty")
            return
        if position == 1:
            self.head = self.head.next
        else:
            current = self.head
            count = 1
            while current.next and count < position - 1:
                count += 1
                current = current.next
            if current.next is None:
                print(f"Position {position} is out of bounds")
            else:
                current.next = current.next.next
    def delete_at_end(self):#single ll
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next and current.next.next:
                current = current.next
            current.next = None
    def display_nodes(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
ll = LinkedList()
ll.insert_at_beginning(30)
ll.insert_at_beginning(20)
ll.insert_at_beginning(10)
ll.insert_at_middle(15,2)
ll.insert_at_end(40)
ll.insert_at_end(50)
ll.delete_node_beg(10)
ll.delete_at_middle(2)
ll.delete_at_end()
ll.display_nodes()