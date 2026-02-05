class Student:
    def __init__(self, nom: str, prenom: str, numero_etudiant: int, credits: int = 0):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = credits
        self.__level = self.__studentEval()  # Initialisation du niveau
    
    # Accesseurs
    def get_nom(self):
        return self.__nom
    
    def get_prenom(self):
        return self.__prenom
    
    def get_numero_etudiant(self):
        return self.__numero_etudiant
    
    def get_credits(self):
        return self.__credits
    
    def get_level(self):
        return self.__level
    
   
    def add_credits(self, credits: int):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__studentEval()  # Mise à jour du niveau
            print(f"{credits} crédits ajoutés avec succès.")
        else:
            print("Erreur : le nombre de crédits doit être supérieur à zéro.")
    
    # Méthode privée pour évaluer le niveau de l'étudiant
    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"
    
    # Méthode pour afficher les informations de l'étudiant
    def studentInfo(self):
        print(f"\n--- Informations de l'étudiant ---")
        print(f"Nom              : {self.__nom}")
        print(f"Prénom           : {self.__prenom}")
        print(f"Numéro étudiant  : {self.__numero_etudiant}")
        print(f"Crédits totaux   : {self.__credits}")
        print(f"Niveau           : {self.__level}")



print("=== Création de l'étudiant John Doe ===")
etudiant1 = Student("Doe", "John", 145)

print("\n=== Ajout de crédits ===")
etudiant1.add_credits(25)
etudiant1.add_credits(30)
etudiant1.add_credits(20)

print(f"\n=== Total de crédits ===")
print(f"Total de crédits : {etudiant1.get_credits()}")


etudiant1.studentInfo()


print("\n\n=== Test avec d'autres étudiants ===")

etudiant2 = Student("Martin", "Alice", 200)
etudiant2.add_credits(95)
etudiant2.studentInfo()

etudiant3 = Student("Dubois", "Pierre", 201)
etudiant3.add_credits(85)
etudiant3.studentInfo()

etudiant4 = Student("Bernard", "Marie", 202)
etudiant4.add_credits(55)
etudiant4.studentInfo()

# invalides
print("\n=== Test d'erreur ===")
etudiant1.add_credits(-10)
etudiant1.add_credits(0)



