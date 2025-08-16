from functools import total_ordering

@total_ordering
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"
    
    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5
    
    def __add__(self, other):
        if not isinstance(other, Vector):
            return TypeError('Operating only supported on instances of Vector')
        
        new_Vector = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        
        return new_Vector
    
    def __mul__(self, scalar):
        if not isinstance(scalar, int) or isinstance(scalar,float):
            return TypeError('Scalar multiplication only supported with int or float')
        
        new_Vactor = Vector(self.x * scalar, self.y * scalar, self.z * scalar)
        
        return new_Vactor
        
    def __rmul__(self, scalar):
        if not isinstance(scalar, int) and not isinstance(scalar, float):
            return TypeError('Scalar multiplication only supported with int or float')
        
        return self.__mul__(scalar)
    
    def __eq__(self, other):
        if not isinstance(other, Vector):
            return TypeError('Comparison only supported on instances of Vector')
        
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __gt__(self, other):
        if not isinstance(other, Vector):
            return TypeError('Comparison only supported on instances of Vector')
        
        return abs(self) > abs(other)
    
    def __bool__(self):
        return abs(self) != 0
    
    def __getitem__(self, item):
        if not isinstance(item, str):
            return TypeError('Indexing only supported with string keys "x", "y", or "z"')
        
        if item.lower() == "x":
            return self.x
        elif item.lower() == "y":
            return self.y
        elif item.lower() == "z":
            return self.z
    
    def __hash__(self):
        return hash((self.x, self.y, self.z))