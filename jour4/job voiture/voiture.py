


class Voiture:
    def __init__(self,marque,modele,annee,nombreporte,prix):
        self.marque =marque
        self.prix=prix
        self.modele=modele
        self.annee=annee
        self.nombreporte=nombreporte
    def immatricule(self):
        print(f"la voiture {self.marque} {self.modele} de l'année {self.annee} avec {self.nombreporte} portes coûte {self.prix} euros.")
