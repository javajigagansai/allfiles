class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.root = None
    def isempty(self):
        return True if self.root is None else False
    def push(self, data):
        newnode = StackNode(data)
        newnode.next = self.root
        self.root = newnode
        print("%d pushed to stack" % data)
    def pop(self):
        if (self.isempty()):
            return float("-inf")
        temp = self.root
        self.root = self.root.next
        popped = temp.data
        return popped
    def peek(self):
        if self.isempty():
            return float("-inf")
        return self.root.data
    def display(self):
        current = self.root
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        return elements
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
print("%d Popped from stack" % (stack.pop()))
print("Top element is %d" % (stack.peek()))
print("Elements present in Stack: ", stack.display())
