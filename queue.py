class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        i = self.first
        while i is not None:
            print(i.value)
            i = i.next

    def enqueue(self, value):  # adds a new node to the end of the queue
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1


queue = Queue(1)
queue.enqueue(2)
queue.enqueue(3)

queue.print_queue()
