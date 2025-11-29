class ListNode:
    def __init__(self, key=-1, value=-1, next=None, prev=None):
        self.key = key
        self.val = value
        self.next = next
        self.prev = prev
    def __str__(self):
        curr = self
        answer = []
      
        while curr:
            answer.append('[' + str(curr.key) + ', ' + str(curr.val)+  ']')
            curr = curr.next
        return '-> '.join(answer)
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        # define everything 
        self.head = ListNode()
        self.tail = ListNode() 

        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}


    def insert(self, node):
        # add to the froint of the list
        hold = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = hold
        hold.prev = node
        



    def remove(self, node):
        # remove the node from the link 
        prev = node.prev
        next = node.next 
        prev.next = next
        next.prev = prev
        

    def get(self, key: int) -> int:
        # print(self.head)
        # get it to the first and return its value
        if key in self.map:

            node = self.map[key]
            self.remove(node)
            self.insert(node)

            return node.val

        return -1 
        

    def put(self, key: int, value: int) -> None:
        # print(self.head)
        # edit if exist 
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.get(node.key)

        # add if not, and also remove the excessive one 
        else:
            node = self.map[key] = ListNode(key=key, value=value)
            self.insert(node)

            if len(self.map) > self.capacity:
                node = self.tail.prev
                self.remove(node)
                self.map.pop(node.key)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)