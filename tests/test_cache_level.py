import unittest
from src.cache_level import Cache

class TestCacheLevel(unittest.TestCase):
    def test_lru_policy(self):
        cache = Cache(2, 'LRU')
        cache.put('A', '1')
        cache.put('B', '2')
        cache.get('A')
        cache.put('C', '3')  # This should evict 'B'
        self.assertIsNone(cache.get('B'))
        self.assertEqual(cache.get('A'), '1')
        self.assertEqual(cache.get('C'), '3')

    def test_lfu_policy(self):
        cache = Cache(2, 'LFU')
        cache.put('A', '1')
        cache.put('B', '2')
        cache.get('A')
        cache.get('A')
        cache.put('C', '3')  # This should evict 'B'
        self.assertIsNone(cache.get('B'))
        self.assertEqual(cache.get('A'), '1')
        self.assertEqual(cache.get('C'), '3')

if __name__ == '__main__':
    unittest.main()
