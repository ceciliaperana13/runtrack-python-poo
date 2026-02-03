class Livre:
    def __init__(self, titre: str, auteur: str, nombre_de_pages: int):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_de_pages = nombre_de_pages

    # ─── Accesseurs ────────────────────────────────────

    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nombre_de_pages(self):
        return self.__nombre_de_pages

    # ─── Mutateurs ─────────────────────────────────────

    def set_titre(self, titre):
        self.__titre = titre
        print(f"Titre changé : {titre}")

    def set_auteur(self, auteur):
        self.__auteur = auteur
        print(f"Auteur changé : {auteur}")

    def set_nombre_de_pages(self, nombre_de_pages):
        if isinstance(nombre_de_pages, int) and nombre_de_pages > 0:
            self.__nombre_de_pages = nombre_de_pages
            print(f"Nombre de pages changé : {nombre_de_pages}")
        else:
            print("Erreur : le nombre de pages doit être un entier positif.")

    # ─── Affichage ─────────────────────────────────────

    def __str__(self):
        return (f"Titre          : {self.__titre}\n"
                f"Auteur         : {self.__auteur}\n"
                f"Nombre de pages: {self.__nombre_de_pages}")




livre1 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 96)
print(livre1)

print("\n--- Modifications ---")
livre1.set_titre("Animal Farm")
livre1.set_auteur("George Orwell")
livre1.set_nombre_de_pages(356)



print("\n--- État final ---")
print(livre1)