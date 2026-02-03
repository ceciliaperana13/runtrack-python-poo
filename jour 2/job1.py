class rectangle:
    def __init__(self, longeur, largeur):
        self._length = longeur
        self._width = largeur
    def afficher(self):
        print(f"Longueur: {self._length}, Largeur: {self._width}")
    def modifier(self, new_length, new_width):
        self._length = new_length
        self._width = new_width    
rectangle1= rectangle(10, 5)
rectangle1.afficher()
rectangle1.modifier(15, 7)
rectangle1.afficher()