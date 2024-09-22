from src.cache_level.py import Cache

class MultilevelCacheSystem:
    def __init__(self):
        self.cache_levels = []

    def add_cache_level(self, size, eviction_policy):
        """Add a new cache level with specified size and eviction policy."""
        new_cache = Cache(size, eviction_policy)
        self.cache_levels.append(new_cache)

    def get(self, key):
        """Retrieve data from the highest-priority cache level."""
        for level in self.cache_levels:
            value = level.get(key)
            if value is not None:
                # Move the data up to the higher cache levels
                self.promote(key, value)
                return value
        return None

    def put(self, key, value):
        """Insert data into the highest-priority cache level."""
        if not self.cache_levels:
            raise Exception("No cache levels available.")
        self.cache_levels[0].put(key, value)

    def promote(self, key, value):
        """Promote data from lower cache level to higher cache levels."""
        # Insert the data in L1 cache, evict if necessary
        for level in reversed(self.cache_levels[:-1]):
            level.put(key, value)

    def remove_cache_level(self, index):
        """Remove a cache level by index."""
        if index < len(self.cache_levels):
            self.cache_levels.pop(index)

    def display_cache(self):
        """Print the current state of each cache level."""
        for i, level in enumerate(self.cache_levels):
            print(f"L{i + 1} Cache: {list(level.cache.items())}")
