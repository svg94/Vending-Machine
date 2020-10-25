import random as r
import os

class Insults:
    def __init__(self):
        file = open(os.path.abspath(os.path.dirname(__file__)) + '/static/text/insults.txt')
        self.insults = file.read().split('\n')
    def getRdmInsult(self):
        rdmNo = r.randint(0, len(self.insults)-2)
        return self.insults[rdmNo]
    def getInsults(self):
        return self.insults
