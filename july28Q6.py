class shape:
    def area(self):
        return 0

class Square(shape):
    def __init__(self,length):
        self.length=length

    def area(self):
        return self.length**2


s=Square(5)

print(s.area())

print(Square.mro())
