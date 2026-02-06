from part import*

class Ship(Part):
    def __init__(self, name, parts):
        super.__init__.part()
        self.name = name
        self.__parts = parts
   

    def display_state(self):
        for part in self.__parts:
            print(part.__str__())
    def add_part(self,part):
        self.parts.append(part)        