class Node:
    def __init__(self,data):
        self.data =data
        self.left = None
        self.right = None
def inordertraversal(root):
    if root is None:
        return
    inordertraversal(root.left)
    print(root.data,end="")
    inordertraversal(root.right)
def preordertraversal(root):
    if root is None:
        return
    print(root.data,end='')
    preordertraversal(root.left)
    preordertraversal(root.right)
def posttraversal(root):
    if root is None:
        return
    preordertraversal(root.left)
    preordertraversal(root.right)
    print(root.data,end='')
def main():
    root=Node(1)
    root.left=Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("inorder traversal:",end='')
    inordertraversal(root)
    print()
    print("preorer traversal:",end='')
    preordertraversal(root)
    print()
    print("postorder traversal:", end='')
    posttraversal(root)
    print()
if __name__ =="__main__":
    main()


