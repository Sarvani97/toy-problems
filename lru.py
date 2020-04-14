class LRUItem(object):
    def __init__(self,key,val):
        self.key = key
        self.val = val

class LRUCache(object):
    def __init__(self):
        self.list = []

    def get(self,key):
        flag = 0
        for l in self.list:
            if(l[0] == key):
                flag = 1
                print(l)
                return
        if(flag == 0):
            return ("Key doesn't exist in the cache")

    def put(self,obj):
        for i in self.list:
            if(i[0] == obj.key):
                return "Key already Exists"
        if(len(self.list) == 5):
            self.list.pop(0)
            self.list.append((obj.key,obj.val))
        else:
            self.list.append((obj.key,obj.val))

    def get_cache(self):
        return self.list




 