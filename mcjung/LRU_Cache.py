# solution Link: https://leetcode.com/submissions/detail/265776551/
# this solution is too slow, may be O(n) of time complexity for put function in worst case
# best solution is using orderd dict on std. lib of python

import queue

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        
        self.LRU_queue = queue.Queue()
        self.LRU_map = dict()
        self.LRU_i = 0
        self.LRU_last = -1
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self._handle_LRU(key)
            return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache and len(self.cache) == self.capacity:
            remove_key = self._get_delete(key, value)
            del self.cache[remove_key]
            self.cache[key] = value                
        else:
            self.cache[key] = value
        self._handle_LRU(key)
    
    def _get_delete(self, key: int, value: int) -> int:
        while True:
            candidate_key = self.LRU_queue.get()
            if (self.LRU_last + 1) != self.LRU_map[candidate_key]:
                self.LRU_last += 1
                continue
            else:
                self.LRU_last += 1
                del self.LRU_map[candidate_key]
                return candidate_key
    
    def _handle_LRU(self, key):
        self.LRU_queue.put(key)
        self.LRU_map[key] = self.LRU_i
        self.LRU_i += 1
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
