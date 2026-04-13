class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def create(self, data):
        if self.head is None:
            self.head = Node(data)
            print(f"Node with data {data} created.")
        else:
            print("Linked list already created.")

    def display(self):
        if self.head is None:
            print("The list is empty.")
            return
        temp = self.head
        print("The list elements are:", end=" ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} at the beginning.")

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(f"Inserted {data} as the first node.")
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        print(f"Inserted {data} at the end.")

    def insert_pos(self, data, position):
        if position < 0:
            print("Invalid position.")
            return
        new_node = Node(data)
        if position == 0:
            self.insert_begin(data)
            return
        temp = self.head
        for i in range(position - 1):
            if temp is None:
                print("Position not found.")
                return
            temp = temp.next
        new_node.next = temp.next if temp else None
        if temp:
            temp.next = new_node
            print(f"Inserted {data} at position {position}.")

    def delete_begin(self):
        if self.head is None:
            print("The list is empty.")
            return
        deleted_data = self.head.data
        self.head = self.head.next
        print(f"Deleted element: {deleted_data}")

    def delete_end(self):
        if self.head is None:
            print("The list is empty.")
            return
        if self.head.next is None:
            deleted_data = self.head.data
            self.head = None
            print(f"Deleted element: {deleted_data}")
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        deleted_data = temp.next.data
        temp.next = None
        print(f"Deleted element: {deleted_data}")

    def delete_pos(self, position):
        if self.head is None:
            print("The list is empty.")
            return
        if position < 0:
            print("Invalid position.")
            return
        if position == 0:
            self.delete_begin()
            return
        temp = self.head
        for i in range(position - 1):
            if temp is None or temp.next is None:
                print("Position not found.")
                return
            temp = temp.next
        if temp.next is None:
            print("Position not found.")
            return
        deleted_data = temp.next.data
        temp.next = temp.next.next
        print(f"Deleted element: {deleted_data}")
def main():
    linked_list = SinglyLinkedList()
    while True:
        print("\n**** SINGLE LINKED LIST OPERATIONS: ****")
        print("1. Create")
        print("2. Display")
        print("3. Insert at the Beginning")
        print("4. Insert at the End")
        print("5. Insert at a Position")
        print("6. Delete at the Beginning")
        print("7. Delete at the End")
        print("8. Delete at a Position")
        print("9. Exit")
        choice = int(input("ENTER THE CHOICE: "))
        if choice == 1:
            data = int(input("ENTER THE DATA VALUE FOR THE NODE: "))
            linked_list.create(data)
        elif choice == 2:
            linked_list.display()
        elif choice == 3:
            data = int(input("ENTER THE DATA VALUE FOR THE NODE: "))
            linked_list.insert_begin(data)
        elif choice == 4:
            data = int(input("ENTER THE DATA VALUE FOR THE NODE: "))
            linked_list.insert_end(data)
        elif choice == 5:
            data = int(input("ENTER THE DATA VALUE FOR THE NODE: "))
            position = int(input("ENTER THE POSITION FOR THE NEW NODE: "))
            linked_list.insert_pos(data, position)
        elif choice == 6:
            linked_list.delete_begin()
        elif choice == 7:
            linked_list.delete_end()
        elif choice == 8:
            position = int(input("ENTER THE POSITION TO BE DELETED: "))
            linked_list.delete_pos(position)
        elif choice == 9:
            print("Exiting...")
            break
        else:
            print("INVALID CHOICE")

if __name__ == "__main__":
    main()
