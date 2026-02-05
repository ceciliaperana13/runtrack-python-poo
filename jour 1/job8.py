import math

class Cercle:
    def __init__(self, rayon):
        """Initialise un cercle avec son rayon"""
        self.rayon = rayon

    def changerRayon(self, nouveau_rayon):
        """Modifie le rayon du cercle"""
        self.rayon = nouveau_rayon

    def circonference(self):
        """Retourne la circonférence du cercle (2 * pi * r)"""
        return 2 * math.pi * self.rayon

    def aire(self):
        """Retourne l'aire du cercle (pi * r²)"""
        return math.pi * self.rayon ** 2

    def diametre(self):
        """Retourne le diamètre du cercle (2 * r)"""
        return 2 * self.rayon

    def afficherInfos(self):
        """Affiche toutes les informations du cercle"""
        print("=" * 35)
        print("       INFORMATIONS DU CERCLE")
        print("=" * 35)
        print(f"  Rayon         : {self.rayon}")
        print(f"  Diamètre      : {self.diametre()}")
        print(f"  Circonférence : {round(self.circonference(), 2)}")
        print(f"  Aire          : {round(self.aire(), 2)}")
        print("=" * 35)



cercle1 = Cercle(4)
cercle2 = Cercle(7)

cercle1.afficherInfos()

cercle2.afficherInfos()        