class Stack:#stack-array
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
        print(f"{item} pushed to stack")
    def pop(self):
        return self.items.pop() if self.items else None
    def peek(self):
        return self.items[-1] if self.items else None
    def str(self):
        return str(self.items)
stack = Stack()
for item in [10, 20, 30, 40]:
    stack.push(str(item))
print(f"{stack.pop()} popped from stack")
print(f"Top element is: {stack.peek()}")