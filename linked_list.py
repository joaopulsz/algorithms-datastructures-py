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

    def append(self, value):  # adds a node to the end o the list
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self.length += 1
        return True

    def pop(self):  # removes and returns the node at the tail of the list
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

    def prepend(self, value):  # adds a new node to the start of the list
        new_node = Node(value)
        if self.length != 0:
            new_node.next = self.head
        else:
            self.tail = new_node
        self.head = new_node
        self.length += 1
        return True

    def pop_first(self):  # removes and returns the node at the head of the list
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
            return item

    def set_value(self, index, value):  # sets the node at the given index to the given value
        item = self.get(index)
        if item:
            item.value = value
            return True
        return False

    def insert(self, index, value):  # inserts a new node at the given index position
        new_node = Node(value)
        if index > self.length or index < 0:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            pre = self.get(index - 1)
            new_node.next = pre.next
            pre.next = new_node
        self.length += 1
        return True


linked_list = LinkedList(1)
linked_list.append(4)

linked_list.insert(1, 3)

linked_list.print_list()
