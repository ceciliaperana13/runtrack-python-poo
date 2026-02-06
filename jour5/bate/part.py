


class Part:
    def __init__(self,name,material):
        self.name=name
        self.material=material
    def getName(self):
        return self.name
    def getmaterial(self):
        return self.material
    def changeMaterial(self,material):
        self.material=material
    def __str__(self):
        return f"Part(name={self.name}, material={self.material})"
        