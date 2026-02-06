import Rectangle



class Forme():
    def __init__(self, aire=0):
        self.aire= aire
    def getAir(self):
        return self.aire    
    def setAir(self, aire):
        self.aire = aire