from datetime import datetime

class LRUItem(object):
    #items in cache.
    def __init__(self,key,data):
        self.key = key
        self.data = data
        self.timestamp = datetime.now()

class LRUCache(object):
    def __init__(self,len,time = None):
        self.len = len
        self.time = time
        self.hash = {}
        self.data_list = []

    def put(self,data):
        pass

    def get(self,data):
        pass

    def get_cache(self):
        pass
