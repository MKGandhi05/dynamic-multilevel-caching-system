import unittest
from src.multilevel_cache import MultilevelCacheSystem

class TestMultilevelCache(unittest.TestCase):
    def setUp(self):
        self.cache_system = MultilevelCacheSystem()
        self.cache_system.add_cache_level(2, 'LRU')
        self.cache_system.add_cache_level(2, 'LFU')

    def test_cache_promotion(self):
        self.cache_system.put('A', '1')
        self.cache_system.put('B', '2')
        self.cache_system.put('C', '3')  # 'A' should be evicted from L1, but stay in L2
        self.assertEqual(self.cache_system.get('A'), '1')  # This should promote 'A' to L1
        self.cache_system.display_cache()

    def test_cache_miss(self):
        self.assertIsNone(self.cache_system.get('Z'))
        self.cache_system.put('Z', '26')
        self.assertEqual(self.cache_system.get('Z'), '26')

if __name__ == '__main__':
    unittest.main()
