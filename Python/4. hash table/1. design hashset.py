class MyHashSet:

    def __init__(self):
        self.hash_table = dict()
        



    def add(self, key: int) -> None:
       
       if self.hash_table.get(key, False) != False:
           return

       self.hash_table[key] = key
       return

    def remove(self, key: int) -> None:
        if self.hash_table.get(key, False):
            del self.hash_table[key]
            return
        return
 
        

    def contains(self, key: int) -> bool:
        if self.hash_table.get(key, False) != False:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(2)
obj.add(3)

obj.remove(2)
param_3 = obj.contains(3)

print(param_3)

# 1 testcase didn't pass so anser is 
class MyHashSet:

    def __init__(self):
        self.hash_table = dict()  # store keys as dictionary keys

    def add(self, key: int) -> None:
        self.hash_table[key] = True   # mark key as present

    def remove(self, key: int) -> None:
        if key in self.hash_table:
            del self.hash_table[key]

    def contains(self, key: int) -> bool:
        return key in self.hash_table
