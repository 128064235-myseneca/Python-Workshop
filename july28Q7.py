class MyException(Exception):
    def __init__(self,message):
        self.message=message

exc=MyException("error")
