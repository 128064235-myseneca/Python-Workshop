class Nepalese:
    pass
class Newari(Nepalese):
    def __init__(self,name):
        self.name=name

    def getName(self):
        return self.name

p=Newari("shubham")
print(p.getName())