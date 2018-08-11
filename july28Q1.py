class Food:
    def __init__(self,name):
        self.name=name

    @property
    def setname(self):
        self.name='momo'

    @setname.setter
    def setname(self,name):
        self.name=name

    def getname(self):
        print(self.name)



F1=Food('MoMo')
F1.getname()
F1.setname="Chowmin"
F1.getname()