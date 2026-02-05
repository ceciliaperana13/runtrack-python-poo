



class Rectangle:
    def __init__(self, longueur=0, largeur=0):
        self.__longueur = longueur
        self.__largeur = largeur
    #guetters
    def getLongueur(self):
        return self.__longueur
    
    def getLargeur(self):
        return self.__largeur
    #setteurs
    def setLongueur(self, longueur):
        self.__longueur = longueur
    def setLargeur(self, largeur):
        self.__largeur = largeur
    #perimetre
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)
    #surface
    def surface(self):
        return self.__longueur * self.__largeur
            