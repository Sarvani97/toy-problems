from datetime import datetime

class LRUItem(obj):
    #items in cache.
    def __init__(self,key,data):
        self.key = key
        self.data = data
        self.timestamp = datetime.now()

class LRUCache(obj):
    def __init__(self,len,delta = None):
        self.len = len
        self.delta = delta
        self.hash = {}
        self.data_list = []

    def insert(self,data):
        pass


    def delete(self,data):
        pass


    def validate(self):
        pass