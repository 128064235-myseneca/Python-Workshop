class Nepal:
    def __init__(self,nationality):
        self.nationality=nationality

    @staticmethod

    def getNationality(nationality):
        print("you are ",nationality)

n=Nepal('nepali')

n.getNationality("american")