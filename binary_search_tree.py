class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        i = self.root
        while True:
            if new_node.value == i.value:
                return False
            if new_node.value > i.value:
                if i.right == None:
                    i.right = new_node
                    return True
                i = i.right
            if new_node.value < i.value:
                if i.left == None:
                    i.left = new_node
                    return True
                i = i.left


tree = BinarySearchTree()
tree.insert(4)
tree.insert(2)
tree.insert(6)

print(tree.root.value)
print(tree.root.right.value)
print(tree.root.left.value)
