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

    def contains(self, value):
        i = self.root
        while i is not None:
            if value > i.value:
                i = i.right
            elif value < i.value:
                i = i.left
            else:
                return True
        return False

    def minimum_value_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node


tree = BinarySearchTree()
tree.insert(4)
tree.insert(2)
tree.insert(6)
tree.insert(7)
tree.insert(3)
tree.insert(5)

print(tree.minimum_value_node(tree.root).value)
print(tree.minimum_value_node(tree.root.right).value)
