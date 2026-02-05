from Rectangle import Rectangle

class Parallepipede(Rectangle):
     def __init__(self, longueur=0, largeur=0, hauteur=0):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

     def getHauteur(self):
        return self.__hauteur
    
    # Mutateur pour hauteur
     def setHauteur(self, hauteur):
        self.__hauteur = hauteur

     def volume(self):
        return self.surface() * self.__hauteur




