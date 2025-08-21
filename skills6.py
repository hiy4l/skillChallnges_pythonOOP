class Tablet:
    models = {"lite": (32, 2), 
              "pro": (64, 3),
              "max": (128, 4)}
    
    
    def __init__(self, model, base_storage=None, added_storage=0, memory=None):
        if model not in self.models:
            raise ValueError(f"Invalid model: {model}. Choose from {self.models}.")
        self.model = model
        self._base_storage = base_storage
        self._added_storage = added_storage
        self._memory = memory
       
        
    @property
    def base_storage(self): 
        self._base_storage = self.models[self.model][0]
        return self._base_storage
    
    
    @property
    def memory(self):
        self._memory = self.models[self.model][1]
        return self._memory
    
    
    @property
    def added_storage(self):
        return self._added_storage
    
    
    @added_storage.setter
    def added_storage(self, storage):
        if (storage + self.base_storage) > 1024:
            raise ValueError("Total storage cannot exceed 1024GB.")
        
        self._added_storage = storage
      
              
    def add_storage(self, additional_storage):
        if (self._added_storage + additional_storage + self._base_storage) > 1024:
            raise ValueError("Total storage cannot exceed 1024GB.")
        
        self._added_storage += additional_storage
     
     
    @property   
    def storage(self):
        return self.base_storage + self.added_storage
       
        
    @storage.setter
    def storage(self, value):
        if value > 1024:
            raise ValueError("Total storage cannot exceed 1024GB.")
        
        self._added_storage = value - self.base_storage
        
    
    def __repr__(self):
        return f"Tablet(model='{self.model}', base_storage={self.base_storage}, added_storage={self.added_storage}, memory={self.memory})"
    