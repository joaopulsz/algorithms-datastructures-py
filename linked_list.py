class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
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

    def append(self, value):  # adds an item to the end o the list
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self.length += 1

    def pop(self):  # removes and returns the item at the tail of the list
        if self.length == 0:
            return None
        item = self.head
        pre = self.head
        while item.next:
            pre = item
            item = item.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return item


linked_list = LinkedList(1)
linked_list.append(3)
linked_list.append(4)

linked_list.pop()

linked_list.print_list()
