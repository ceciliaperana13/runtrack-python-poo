class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def getPrixHT(self):
        return self.prixHT

    def prixTTC(self):
        return round(self.prixHT * (1 + self.TVA / 100), 2)

    def calculerPrixTTC(self):
        return self.prixTTC()

    def afficher(self):
        return (
            f"Nom      : {self.nom}\n"
            f"Prix HT  : {self.getPrixHT()} €\n"
            f"TVA      : {self.TVA} %\n"
            f"Prix TTC : {self.calculerPrixTTC()} €"
        )

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom
        return self.nom


# Création et affichage du produit
produit = Produit("Ordinateur", 1000, 20)
print(produit.afficher())

# Modification du nom
produit.modifierNom("Ordinateur Portable")
print("\nApres modification :")
print(produit.afficher())