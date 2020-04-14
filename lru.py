class LRUItem(object):
    #items in cache.
    def __init__(self,key,val):
        self.key = key
        self.val = val

class LRUCache(object):
    def __init__(self):
        self.data_list = []

    def put(self,data):
        for d in self.data_list:
            if d[0] == data.key:
                return "key already exists"
        if(len(self.data_list) == 4):
            self.data_list.pop(0)
            self.data_list.append((data.key,data.val))
        else:
            self.data_list.append((data.key,data.val))

    def get(self,key):
        for i in self.data_list:
            if i[0] == key:
                print("key already exists")
            else:
                print("key doesn't exist")

    def get_cache(self):
        return self.data_list

