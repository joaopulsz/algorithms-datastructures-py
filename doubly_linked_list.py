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

    def get(self, index):  # returns the node at the given index
        if index >= self.length or index < 0:
            return None
        else:
            if index < self.length / 2:
                item = self.head
                for _ in range(index):
                    item = item.next
            else:
                item = self.tail
                for _ in range(self.length - 1, index, -1):
                    item = item.previous
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
            pre.next.previous = new_node
            new_node.previous = pre
            pre.next = new_node
        self.length += 1
        return True

    def remove(self, index):  # removes the node at the given index
        if index >= self.length or index < 0:
            return None
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        item = self.get(index)
        item.next.previous = item.previous
        item.previous.next = item.next
        item.next = None
        item.previous = None
        self.length -= 1
        return item


doubly_linked_list = DoublyLinkedList(5)
doubly_linked_list.append(3)
doubly_linked_list.append(6)
doubly_linked_list.append(4)

doubly_linked_list.remove(1)

doubly_linked_list.print_list()
