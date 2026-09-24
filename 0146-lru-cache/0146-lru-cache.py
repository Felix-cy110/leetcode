class DLinkedNode:
    def __init__(self, key=0,value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.cache = dict()
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.value
    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = DLinkedNode(key, value)
            self.addToHead(node)
            self.size += 1
            self.cache[key] = node
            if self.size > self.capacity:
                removed = self.removeTail()
                self.size -= 1
                self.cache.pop(removed.key)
        else:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    def moveToHead(self, node):
        self.remove(node)
        self.addToHead(node)

    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def addToHead(self,node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def removeTail(self):
        node = self.tail.prev
        self.remove(node)
        return node
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)