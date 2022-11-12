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

    def delete_node(self, current_node, value):
        if current_node is None:
            return None
        elif value < current_node.value:
            current_node.left = self.delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.delete_node(current_node.right, value)
        else:
            if not current_node.left and not current_node.right:
                current_node = None
            elif not current_node.left:
                current_node = current_node.right
            elif not current_node.right:
                current_node = current_node.left
            else:
                item = self.minimum_value_node(current_node.right)
                current_node.value = item.value
                current_node.right = self.delete_node(
                    current_node.right, item.value)
        return current_node

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

    def breadth_first_search(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results
            