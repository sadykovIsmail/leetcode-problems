class MyHashSet:

    def __init__(self):
        self.hash_table = dict()
        



    def add(self, key: int) -> None:
       
       if self.hash_table.get(key, False) != False:
           return

       self.hash_table[key] = key
       return

    def remove(self, key: int) -> None:
        
 
        

    def contains(self, key: int) -> bool:
        if self.hash_table.get(key, False) != False:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(2)
# obj.remove(key)
param_3 = obj.contains(1)

print(param_3)