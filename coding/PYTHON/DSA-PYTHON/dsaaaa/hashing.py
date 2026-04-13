class SimpleHashTable:#hashing
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    def hash_function(self, key):
        return hash(key) % self.size
    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index] = value
        print(f"Inserted {key}: {value} at index {index}")
    def search(self, key):
        index = self.hash_function(key)
        return self.table[index]
hash_table = SimpleHashTable(10)
hash_table.insert("a", 10)
hash_table.insert("b", 20)
hash_table.insert("c", 30)
print("Value for 'a':", hash_table.search("a"))
print("Value for 'b':", hash_table.search("b"))
print("Value for 'c':", hash_table.search("c"))
