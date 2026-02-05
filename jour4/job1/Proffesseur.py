from jour4.job1.Personne import Personne

class Professeur(Personne):
    def __init__(self, age=14, matiereEnseignee=None):
        super().__init__(age)  
        self.__matiereEnseignee = matiereEnseignee  # Attribut privé
    
    def enseigner(self):
        print("Le cours va commencer")