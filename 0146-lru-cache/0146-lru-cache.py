class Node:
    def __init__(self, key=-1, val=-1, next=None, prev=None):
        self.val = val # key, val
        self.key = key
        self.next = next
        self.prev = prev


class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.map = {} # key : node
    
    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        self.map.pop(node.key)
        return node
    
    def insert(self, key, val):

        node = Node(key, val, self.head.next, self.head)
        self.head.next = node
        node.next.prev = node
        self.map[key] = node
        return node

        
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        node = self.remove(self.map[key])
        self.insert(node.key, node.val)
        
        return node.val
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.map:
            self.map[key].val = value
            self.get(key)
        else:
            self.insert(key, value)
            # if we have no enough size 
            if len(self.map) > self.capacity:
                self.remove(self.tail.prev)



# 2, 4, 1, 3

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)