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

    def prepend(self, value):  # inserts new node to the start of the list
        new_node = Node(value)
        if self.length != 0:
            self.head.previous = new_node
            new_node.next = self.head
        else:
            self.tail = new_node
        self.head = new_node
        self.length += 1
        return True

    def pop_first(self):  # removes and returns the node at the start of the list
        if self.length == 0:
            return None
        item = self.head
        self.head = self.head.next
        if self.head:
            self.head.previous = None
        item.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return item


doubly_linked_list = DoublyLinkedList(5)
doubly_linked_list.append(3)

doubly_linked_list.prepend(4)

doubly_linked_list.pop_first()
doubly_linked_list.pop_first()

doubly_linked_list.print_list()
