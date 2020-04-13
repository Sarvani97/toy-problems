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

    def insert(self,data):
        if data.key in self.hash:
            #move the visited data(if in the list) in the list to the top.
            data_idx = self.data_list.index(data)
            self.data_list[:] = self.data_list[:data_idx] + self.data_list[data_idx + 1:]
            self.data_list.insert(0,data)

        else:
            #remove the last item if the size exceeds
            if len(self.data_list) > self.len:
                self.remove(self.data_list[-1])
            #append to the front of the list
            self.hash[data.key] = data
            self.data_list.insert(0,data)



    def delete(self,data):
        del self.hash[data.key]
        del self.data_list[self.data_list.index(data)]



    def validate(self):
        def oldData():
            now = datetime.now()
            for d in data_list:
                timeLeft = now - data.timestamp
                if timeLeft.seconds > self.time:
                    yield data
        map(lambda x: self.remove(data), oldData())
    

