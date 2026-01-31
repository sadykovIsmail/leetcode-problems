class MyHashMap:

    def __init__(self):
        self.hashMap = dict()
        

    def put(self, key: int, value: int) -> None:
        self.hashMap[key] = value
        return self.hashMap

    def get(self, key: int) -> int:
        if key in self.hashMap:
            return self.hashMap[key]
        return - 1

    def remove(self, key: int) -> None:
        if key in self.hashMap:
            del self.hashMap[key]
        return


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
print(obj.put(1,"a"))
print(obj.put(1, "b"))


print(obj.get(1))
obj.remove(2)

