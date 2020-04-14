from lru import *

e1 = LRUItem(1,"one")
e2 = LRUItem(2,"two")
e3 = LRUItem(3,"three")
e4 = LRUItem(4,"four")
e5 = LRUItem(5,"five")
e6 = LRUItem(6,"six")

class LRUTest:
    cache = LRUCache()
    cache.put(e1)
    res = cache.get_cache()
    assert res == [(1, 'one')]
    cache.put(e2)
    cache.put(e3)
    cache.put(e4)
    res = cache.get(7)
    assert res == "Key doesn't exist in the cache"
    cache.put(e5)
    res = cache.get_cache()
    assert res == [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')]
    cache.put(e6)
    res = cache.get_cache()
    assert res == [(2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'), (6, 'six')]
    res = cache.put(e5)
    assert res == "Key already Exists"
    print("All test Cases passed")
