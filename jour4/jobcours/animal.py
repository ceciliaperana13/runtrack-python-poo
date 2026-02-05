
from jour4.jobcours.chien import Chien
from jour4.jobcours.oiseau import Oiseau


class Animal:
    def __init__(self, chien, oiseau):
       
        self.__chien = chien
        self.__oiseau = oiseau

    def se_deplacer(self):
        self.__chien.se_deplacer()
        self.__oiseau.se_deplacer()

        
            

chien1 = Chien()
oiseau1 = Oiseau()