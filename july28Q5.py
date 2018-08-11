class Rectangle:
    def __init__(self,length,breadth):
        self.lenght=length
        self.breadth=breadth

    def calcArea(self):
        return self.lenght*self.breadth

    @property
    def getLB(self):
        return (self.lenght,self.breadth)

r1=Rectangle(5,4)

print("area::",r1.calcArea())

print("Leangth and breadth::",r1.getLB)
