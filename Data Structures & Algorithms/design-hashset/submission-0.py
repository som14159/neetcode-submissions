class MyHashSet:

    def __init__(self):
        self.s = {}

    def add(self, key: int) -> None:
        self.s[str(key)] = True

    def remove(self, key: int) -> None:
        if str(key) in self.s:
            self.s[str(key)] = False

    def contains(self, key: int) -> bool:
        if str(key) not in self.s or not self.s[str(key)]:
            return False
        return True


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)