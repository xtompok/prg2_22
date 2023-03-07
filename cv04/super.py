class Rectangle:
    def __init__(self,ll,ur) -> None:
        self.ll = ll
        self.ur = ur
        
    def area(self):
        return abs((self.ur[0]-self.ll[0])*(self.ur[1]-self.ll[1]))

class ColorRectangle(Rectangle):
    def __init__(self,ll,ur,color) -> None:
	# Call superclass initializer to init common attributes
        super().__init__(ll,ur)
	# Set own attribute(s)
        self.color = color

	# Equivalent code, but don't use it
	#self.ll = ll
	#self.ur = ur
	#self.color = color

    # area() method is defined in superclass and it evaluate 
    # the same way in this class so we don't need to redefine it

r = Rectangle([0,0],[10,10])
cr = ColorRectangle([5,5], [-25,10], "black")

print(f"{r.area()=}")
print(f"{cr.area()=}")

