class MyHashSet:

    def __init__(self):
        self.hash_table = dict()


    def add(self, key: int) -> None:
        actual_key = key % 2
        self.hash_table[actual_key] = key
        return self.hash_table.items()

    # def remove(self, key: int) -> None:
        

    # def contains(self, key: int) -> bool:
        


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(2)
# obj.remove(key)
# param_3 = obj.contains(key)

print(obj)