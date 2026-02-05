class Ville:
    def __init__(self,nom, population):
        self.__nom=nom
        self.__population=population
       
    def get_nom(self):
        return self.__nom
    def set_nom(self, nom):
        self.__nom = nom
    def incrementer_population(self,nombre):
        if nombre >0:
            self.__population += nombre
                





class Personne:
    def __init__(self, nom, age):
        self.__nom = nom
        self.__age = age
    def get_nom(self):
        return self.__nom
    def set_nom(self, nom):
        self.__nom = nom
        personne1 =Personne("john")
    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age
        personne1 =Personne( 45)

print(personne1.get_nom())
print(personne1.get_age())        



        