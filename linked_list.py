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

    def prepend(self, value):  # adds value to the start of the list
        new_node = Node(value)
        if self.length != 0:
            new_node.next = self.head
        else:
            self.tail = new_node
        self.head = new_node
        self.length += 1

    def pop_first(self):  # removes and returns the item at the head of the list
        if self.length == 0:
            return None
        item = self.head
        self.head = self.head.next
        item.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return item

    def get(self, index):  # returns the node at the given index
        if index >= self.length or index < 0:
            return None
        else:
            item = self.head
            for _ in range(index):
                item = item.next
            return item.value


linked_list = LinkedList(1)
linked_list.append(4)
linked_list.append(5)
linked_list.prepend(8)

print(linked_list.get(3))


# linked_list.print_list()
