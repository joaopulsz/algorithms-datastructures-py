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


doubly_linked_list = DoublyLinkedList(5)

doubly_linked_list.print_list()
