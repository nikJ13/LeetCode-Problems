class ListNode:
    def __init__(self,prev=None,next=None,val=None, key=None):
        self.prev = prev
        self.next = next
        self.val = val
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        # key: key, and value: LinkedList Obj location
        self.cache_dict = {}
        self.capacity = capacity
        self.ptr_recent = ListNode(val = -1)
        self.ptr_oldest = ListNode(val = -1)
        self.ptr_recent.next = self.ptr_oldest
        self.ptr_oldest.prev = self.ptr_recent

    def get(self, key: int) -> int:
        # dictionary
        if key in self.cache_dict:
            obj = self.cache_dict[key]
            # if we get a key, then it has to be marked recently used too
            self.mark_used(obj)
            return obj.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache_dict:
            obj = self.cache_dict[key]
            obj.val = value
            self.mark_used(obj)
        else:
            # need to first check if there is still capacity left
            if len(self.cache_dict)==self.capacity:
                node_to_be_deleted = self.ptr_oldest.prev
                deleted = self.delete(node_to_be_deleted)
                del self.cache_dict[node_to_be_deleted.key]
            new_node = ListNode(key=key, val=value)
            self.cache_dict[key] = new_node
            self.add(new_node)
        
    def mark_used(self,node):
        # we have to make the ptr_recent point to node
        curr_node = self.delete(node)
        self.add(curr_node)

    def delete(self,node):
        curr_node = self.ptr_recent.next
        while curr_node is not node:
            curr_node = curr_node.next
        next_node = curr_node.next
        prev_node = curr_node.prev
        prev_node.next, next_node.prev = next_node, prev_node
        curr_node.next, curr_node.prev = None, None
        return curr_node
    
    def add(self,node):
        # it will always be added to the recent
        old_recent = self.ptr_recent.next
        old_recent.prev = node
        node.next = old_recent
        self.ptr_recent.next = node
        node.prev = self.ptr_recent




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)