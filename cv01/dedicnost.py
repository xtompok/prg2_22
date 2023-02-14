from abc import abstractmethod, ABC
from turtle import penup, pendown, dot, setpos, setheading, forward, left, exitonclick

class GraphicObject(ABC):
    @abstractmethod
    def draw(self):
        pass
    
    @abstractmethod
    def bounding_box(self) -> tuple:
        """Returns 4-tuple (llx, lly, urx, ury) where ll is lower-left
    	corner and ur is upper-right corner."""
        pass
        
    
    def bounding_box_area(self):
        bbox = self.bounding_box()
        return (bbox[2]-bbox[0])*(bbox[3]-bbox[1])

class Point(GraphicObject):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def draw(self):
        penup()
        setpos(self.x,self.y)
        pendown()
        dot(5)
    
    def bounding_box(self) -> tuple:
        return (self.x, self.y, self.x, self.y)

class Rectange(GraphicObject):
    def __init__(self,llx,lly,w,h):
        self.llx = llx
        self.lly = lly
        self.width = w
        self.height = h
    
    def draw(self):
        penup()
        setpos(self.llx, self.lly)
        pendown()
        setheading(0)
        forward(self.width)
        left(90)
        forward(self.height)
        left(90)
        forward(self.width)
        left(90)
        forward(self.height)

    def bounding_box(self) -> tuple:
        return (self.llx, self.lly, self.llx + self.width, self.lly + self.height)

pt = Point(10,10)
rect = Rectange(5,5,20,40) #llx,lly, width, height 

pt.draw()
print(pt.bounding_box_area()) # -> 0

rect.draw()
print(rect.bounding_box_area()) # -> 800

exitonclick()