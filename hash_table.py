class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        hash = 0
        for letter in key:
            hash = (hash + ord(letter) * 23) % len(self.data_map)
        return hash

    def print_table(self):
        for key, value in enumerate(self.data_map):
            print(key, ": ", value)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])


hash_table = HashTable()

hash_table.set_item('guitars', 3)
hash_table.set_item('pianos', 1)
hash_table.set_item('flutes', 6)

hash_table.print_table()
