# Dynamic Multilevel Caching System

## Overview
This project implements a dynamic multilevel caching system with support for both LRU (Least Recently Used) and LFU (Least Frequently Used) eviction policies. The system is designed to be flexible, efficient, and thread-safe, allowing for concurrent access and modification.

## Features
- **Multiple Cache Levels**: Support for dynamic addition and removal of cache levels.
- **Eviction Policies**: Choose between LRU (Least Recently Used) and LFU (Least Frequently Used) policies.
- **Thread Safety**: All operations are thread-safe, allowing for concurrent access.
- **Cache Promotion**: Efficiently promotes data to higher cache levels on access.

## Classes and Methods

### `class Cache`
Represents an individual cache level with a specified size and eviction policy.
- `__init__(self, size, eviction_policy)`: Initializes the cache with a given size and eviction policy.
- `get(self, key)`: Retrieves the value associated with the key from the cache.
- `put(self, key, value)`: Adds or updates the key-value pair in the cache.
- `display(self)`: Returns the current state of the cache.

### `class MultilevelCacheSystem`
Manages multiple cache levels and allows dynamic addition, removal, and access of caches.
- `addCacheLevel(self, size, eviction_policy)`: Adds a new cache level with the given size and eviction policy.
- `removeCacheLevel(self, level)`: Removes the specified cache level.
- `get(self, key)`: Retrieves the value for the key from the highest priority cache.
- `put(self, key, value)`: Inserts the key-value pair into the highest priority cache.
- `displayCache(self)`: Displays the current state of all cache levels.

## Running the Project
1. Clone the repository.
2. Install Python (if not already installed).
3. Run the tests using:
   ```bash
   python test_cache.py
