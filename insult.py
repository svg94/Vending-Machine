import random as r
class Insults:
    def __init__(self):
        file = open("static/text/insults.txt")
        self.insults = file.read().split(',')
    def getRdmInsult(self):
        rdmNo = r.randint(0, len(self.insults))
        return self.insults[rdmNo]
