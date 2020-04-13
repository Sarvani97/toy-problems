from lru import *
from time import sleep

def output(cache):
    for i,data in enumerate(cache.data_list):
        print("index: {0} "
              "key: {1} "
              "data: {2} "
              "timestamp: {3}".format(i,data.key,data.data,data.timestamp))

e1 = LRUItem(1,'one')
e2 = LRUItem(2,'two')
e3 = LRUItem(3,'three')

print("Initial items")
cache = LRUCache(len = 3, time = 5)
cache.insert(one)
cache.insert(two)
cache.insert(three)
output(cache)
print("\n")

print("Insert an existing item")
cache.insert(one)
output(cache)
print("\n")


print("Validating items after sometime")
sleep(6)
cache.validate()
output(cache)
print("\n")