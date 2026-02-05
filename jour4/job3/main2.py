from jour4.job3.Rectangle import Rectangle
from jour4.job3.Parallelepipede import Parallepipede



print ("\n test rectangle")
rect= Rectangle(10, 5)


print("Perimetre du rectangle:", rect.perimetre())
print("Surface du rectangle:", rect.surface())

print ("\n test parallelepipede")
para= Parallepipede(10, 5, 3)

print("Volume du parallelepipede:", para.volume())