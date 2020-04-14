from lru import *

e1 = (1,'one')
e2 = (2,'two')
e3 = (3,'three')
e4 = (4,'four')
e5 = (5,'five')
e6 = (6,'six')
e7 = (7,'seven')

class LruTest:
    cache = LRUCache()
    cache.put(e1)

    result = cache.get_cache()
    assert result == [(1,'one')]

    cache.put(e2)
    cache.put(e3)
    cache.put(e4)
    cache.put(e5)

    result = cache.get(10)

    assert result == "No such key"

    cache.put(e6)
    result == cache.get_cache()
    assert result == [(1,'one'),(2,'two'),(3,'three'),(4,'four'),(5,'five'),(6,'six')]

    result = cache.put(e5)
    assert result == "key already exists"

    print("All test cases passed")



