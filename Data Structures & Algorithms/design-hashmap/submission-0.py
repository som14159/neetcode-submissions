class MyHashMap:

    def __init__(self):
        self.s = {}

    def put(self, key: int, value: int) -> None:
        self.s[key] = value

    def get(self, key: int) -> int:
        return -1 if key not in self.s else self.s[key]

    def remove(self, key: int) -> None:
        self.s[key] = -1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)