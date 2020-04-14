class LRUItem(object):
    #items in cache.
    def __init__(self,key,val):
        self.key = key
        self.val = val

class LRUCache(object):
    def __init__(self):
        self.data_list = []

    def put(self,obj):
        for d in self.data_list:
            if d[0] == obj.key:
                #print("key already exists")
                return ("key already exists")
        if(len(self.data_list) == 4):
            self.data_list.pop(0)
            self.data_list.append((obj.key,obj.val))
        else:
            self.data_list.append((obj.key,obj.val))

    def get(self,key):
        flag = False
        for d in self.data_list:
            if d[0] == key:
                flag = True
                return
        if flag == False:
            #print("No such key")
            return ("No such key")

    def get_cache(self):
        #print(str(self.data_list)[1:-1])
        return self.data_list

