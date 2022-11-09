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

    def append(self, value):
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self.length += 1
        return True

    def pop(self):
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

    def prepend(self, value):
        new_node = Node(value)
        if self.length != 0:
            new_node.next = self.head
        else:
            self.tail = new_node
        self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        item = self.head
        self.head = self.head.next
        item.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return item

    def get(self, index):
        if index >= self.length or index < 0:
            return None
        else:
            item = self.head
            for _ in range(index):
                item = item.next
            return item

    def set_value(self, index, value):
        item = self.get(index)
        if item:
            item.value = value
            return True
        return False

    def insert(self, index, value):
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

    def remove(self, index):
        if index >= self.length or index < 0:
            return None
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        item = pre.next
        pre.next = item.next
        item.next = None
        self.length -= 1
        return item

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        post = self.head
        pre = None
        for _ in range(self.length):
            post = temp.next
            temp.next = pre
            pre = temp
            temp = post
