class livre:
    def __init__(self, titre,auteur, nombre_de_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_de_pages = nombre_de_pages

    def afficher_attributs(self):
        print(f"Titre: {self.__titre}, Auteur: {self.__auteur}, Nombre de pages: {self.__nombre_de_pages}")
    def modifier_attributs(self, new_titre, new_auteur, new_nombre_de_pages):
        self.__titre = new_titre
        self.__auteur = new_auteur
        self.__nombre_de_pages = new_nombre_de_pages