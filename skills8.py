from collections import UserDict

class BidirectionalDict(UserDict):
    def __init__(self, *args, **kwargs):
        self.forward = dict(*args, **kwargs)
        self.backward = {}
        
        for k in self.forward:
            v = self.forward[k]
            self.backward[v] = k
        
        self.complete_dicts = self.forward | self.backward
        
    def __getitem__(self, key):
        return self.complete_dicts[key]
    
    def __len__(self):
        return len(self.complete_dicts) // 2
    
    def __setitem__(self, key, value):
        old_value = self.complete_dicts.get(key)
        self.complete_dicts[key] = value
        self.complete_dicts[value] = self.complete_dicts.pop(old_value)
        
    def __delitem__(self, key):
        value = self.complete_dicts[key]
        del self.complete_dicts[value] 
        del self.complete_dicts[key]
    
    def __repr__(self):
        return f"{self.complete_dicts}"