import math
class Circle:
    def __init__(self,radius):
        self.radius=radius

    def calcArea(self):
        return math.pi*self.radius**2

    @property
    def getRadius(self):
        return self.radius

c=Circle(5)
print("Area::",c.calcArea())

print("Radius::",c.getRadius)
