class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        i = self.top
        while i is not None:
            print(i.value)
            i = i.next

    def push(self, value):
        new_node = Node(value)
        if self.height != 0:
            new_node.next = self.top
        self.top = new_node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        item = self.top
        self.top = item.next
        item.next = None
        self.height -= 1
        return item
