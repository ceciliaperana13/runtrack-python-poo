from jour4.job3.Rectangle import Rectangle

class Parallepipede(Rectangle):
     def __init__(self, longueur=0, largeur=0, hauteur=0):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur
     def volume (self):
        return self.getlongueur()*self.getlargeur()*self.__hauteur    




