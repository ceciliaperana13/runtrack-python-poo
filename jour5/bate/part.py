

class Part:
    """Classe représentant une pièce de bateau"""
    
    def __init__(self, name, material):
        self.name = name
        self.material = material
    
    def change_material(self, new_material):
        """Modifie le matériau de la pièce"""
        old_material = self.material
        self.material = new_material
        return old_material
    
    def __str__(self):
        return f"{self.name} en {self.material}"