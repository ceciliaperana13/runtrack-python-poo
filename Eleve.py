from Personne import Personne

class Eleve(Personne):
    def aller_en_cours(self):
        print("je vais en cours")
    def afficherAge(self):
        print(f"J'ai {self.age} ans")