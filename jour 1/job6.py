class Animal:
    def __init__(self, age, prenoms=None):
        self.age = age
        self.prenoms = prenoms
    def vieillir(self):
        
        self.age += 1
        print("L'animal a vieilli. Nouvel âge :", self.age)
        return self 
    def nommer(self,prenoms):
        self.prenoms = prenoms
        print("le nom de L'animal est :",self.prenoms)
        return self

Animal(0).vieillir().nommer("Luna")