class Point3D:
    __slots__ = ("x", "y", "z")
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __repr__(self):
        return f"{self.__name__}"
        
    def __repr__(self):
        if self.__slots__.__len__() == 3:
            return f"{self.__class__.__name__}(x = {self.x}, y = {self.y}, z = {self.z})"
        else:
            return f"{self.__class__.__name__}(x = {self.x}, y = {self.y}, z = {self.z}, {self.__slots__} = \"{self.__getattribute__(self.__slots__.__str__())}\""
    
class ColoredPoint(Point3D):
    __slots__ = "color"
    
    def __init__(self, x, y, z, color = "black"):
        super().__init__(x, y, z)
        self.color = color
        

class ShapedPoint(Point3D):
    __slots__ = "shape"
    
    def __init__(self, x, y, z, shape = "sphere"):
        super().__init__(x, y, z)
        self.shape = shape