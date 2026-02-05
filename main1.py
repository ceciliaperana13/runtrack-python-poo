from Personne import Personne
from Eleve import Eleve
from Proffesseur import Professeur

Personne1 = Personne()
eleve1 = Eleve()
prof1 = Professeur()

print("Âge par défaut de l'élève :")
eleve1.afficherAge()  
print("\n Action de l'eleve:")
eleve1.aller_en_cours()
print("\n Modification de l'age")
eleve1.modifierAge(15)
print("\n Age modifier de l'eleve : ")
eleve1.afficherAge()

print("\n--- Actions du professeur ---")
prof1=Professeur(40)
prof1.Bonjour()
prof1.enseigner()