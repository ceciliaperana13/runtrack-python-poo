class Personnes:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

personne1 = Personnes("Doe", "John")
personne2 = Personnes("Jean","Dupond")
print("je suis",personne1.nom, personne1.prenom)
print("je suis",personne2.nom, personne2.prenom)