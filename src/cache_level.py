from collections import OrderedDict
import heapq

class Cache:
    def __init__(self, size, eviction_policy):
        self.size = size
        self.eviction_policy = eviction_policy
        self.cache = OrderedDict()
        self.frequency = {}  # For LFU
        self.min_heap = []  # For LFU
    
    def get(self, key):
        if key in self.cache:
            if self.eviction_policy == 'LFU':
                self.frequency[key] += 1
                heapq.heappush(self.min_heap, (self.frequency[key], key))
            else:  # LRU or other policies
                self.cache.move_to_end(key)
            return self.cache[key]
        return None

    def put(self, key, value):
        if key in self.cache:
            if self.eviction_policy == 'LFU':
                self.frequency[key] += 1
                heapq.heappush(self.min_heap, (self.frequency[key], key))
            self.cache[key] = value
            return

        if len(self.cache) >= self.size:
            self.evict()
        self.cache[key] = value
        if self.eviction_policy == 'LFU':
            self.frequency[key] = 1
            heapq.heappush(self.min_heap, (1, key))

    def evict(self):
        if self.eviction_policy == 'LRU':
            # Remove the first element, which is the least recently used
            self.cache.popitem(last=False)
        elif self.eviction_policy == 'LFU':
            # Remove the least frequently used element
            while self.min_heap:
                freq, key = heapq.heappop(self.min_heap)
                if self.frequency[key] == freq:
                    self.cache.pop(key, None)
                    self.frequency.pop(key, None)
                    break
