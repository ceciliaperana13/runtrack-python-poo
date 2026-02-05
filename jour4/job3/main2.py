from Rectangle import Rectangle
from Parallelepipede import Parallepipede



print ("\n ----test rectangle----")
rect= Rectangle(10, 5)


print("Perimetre du rectangle:", rect.perimetre())
print("Surface du rectangle:", rect.surface())

print ("\n ----test parallelepipede-----")
para= Parallepipede(10, 5, 3)



print(f"Longueur : {para.getLongueur()}")
print(f"Largeur : {para.getLargeur()}")
print(f"Hauteur : {para.getHauteur()}")
print(f"Périmètre de la base : {para.perimetre()}")
print(f"Surface de la base : {para.surface()}")
print(f"Volume : {para.volume()}")



para.setLongueur(12)
para.setLargeur(6)
para.setHauteur(4)

print(f"\nAprès modification :")
print(f"Longueur : {para.getLongueur()}")
print(f"Largeur : {para.getLargeur()}")
print(f"Hauteur : {para.getHauteur()}")
print(f"Volume : {para.volume()}")