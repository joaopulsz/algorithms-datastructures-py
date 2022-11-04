class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        i = self.head
        while i is not None:
            print(i.value)
            i = i.next

    def append(self, value):  # adds a node to the end o the list
        new_node = Node(value)
        if self.tail:
            new_node.previous = self.tail
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self.length += 1
        return True

    def pop(self):  # removes and returns the node at the tail of the list
        if self.length == 0:
            return None
        item = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None
            item.previous = None
        self.length -= 1
        return item


doubly_linked_list = DoublyLinkedList(5)
doubly_linked_list.append(3)

doubly_linked_list.pop()


doubly_linked_list.print_list()