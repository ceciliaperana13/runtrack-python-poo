



class rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
    
    def perimetre(self):
        return 2 * (self.longueur + self.largeur)
    
    def surface(self):
        return self.longueur * self.largeur