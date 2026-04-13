class Node:
    def __init__(self, data):
    self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last
    def insert_after(self, prev_data, data):
        current = self.head
        while current:
            if current.data == prev_data:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                new_node.prev = current
                if new_node.next:
                    new_node.next.prev = new_node
                return
            current = current.next
        print(f"Node with data {prev_data} not found")

    def insert_before(self, next_data, data):
        current = self.head
        while current:
            if current.data == next_data:
                new_node = Node(data)
                new_node.next = current
                new_node.prev = current.prev
                if current.prev:  # Update the previous node's next pointer
                    current.prev.next = new_node
                else:  # Inserting before the head
                    self.head = new_node
                current.prev = new_node
                return
            current = current.next
        print(f"Node with data {next_data} not found")
    def delete_head(self):
        if not self.head:
            print("The list is empty")
            return
        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None
    def delete_last(self):
        if not self.head:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        last = self.head
        while last.next:
            last = last.next
        last.prev.next = None
    def delete_by_value(self, data):
        current = self.head
        if current and current.data == data:
            self.delete_head()
            return
        while current and current.data != data:
            current = current.next
        if current is None:
            print(f"Node with data {data} not found")
            return
        if current.next is None:
            self.delete_last()
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
    def display_forward(self):
        current = self.head
        if not current:
            print("List is empty")
            return
        print("List (forward):", end=" ")
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
    def display_backward(self):
        current = self.head
        if not current:
            print("List is empty")
            return
        while current.next:
            current = current.next
        print("List (backward):", end=" ")
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.append(30)
    dll.display_forward()
    print("\nInserting 5 at beginning")
    dll.insert_at_beginning(5)
    dll.display_forward()
    print("\nInserting 25 after 20:")
    dll.insert_after(20, 25)
    dll.display_forward()
    print("\nInserting 28 before 30")
    dll.insert_before(30, 28)
    dll.display_forward()
    print("\nDeleting head node")
    dll.delete_head()
    dll.display_forward()
    print("\nDeleting last node:")
    dll.delete_last()
    dll.display_forward()
    print("\nDeleting last node with value 25:")
    dll.delete_by_value(25)
    dll.display_forward()
    print("\nDisplaying list backward")
    dll.display_backward()
    print("\nAttempting to delete node with value 100 (non-existent):")
    dll.delete_by_value(100)
    dll.display_forward()