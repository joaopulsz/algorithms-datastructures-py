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


hash_table = HashTable()

hash_table.print_table()
