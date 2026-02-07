from part import*
from ship import*
from racingship import*


def display_menu():
    """Affiche le menu principal"""
    print("\n" + "="*50)
    print("         GESTION DU BATEAU - MENU PRINCIPAL")
    print("="*50)
    print("1. Afficher l'état du bateau")
    print("2. Ajouter une pièce")
    print("3. Remplacer une pièce")
    print("4. Modifier le matériau d'une pièce")
    print("5. Afficher l'historique")
    print("6. Démonstration du passage par référence")
    print("7. Quitter")
    print("="*50)


def demonstration_reference():
    """Démontre le passage par référence des objets Part"""
    print("\n" + "="*50)
    print("   DÉMONSTRATION DU PASSAGE PAR RÉFÉRENCE")
    print("="*50)
    
    # Création d'une pièce
    mast = Part("Mât", "Bois")
    print(f"\n1. Création de la pièce: {mast}")
    print(f"   Adresse mémoire: {id(mast)}")
    
    # Création d'un bateau avec cette pièce
    boat = Ship("Démo", [mast])
    
    # Modification via la méthode du bateau
    print(f"\n2. Modification via ship.change_part('Mât', 'Aluminium')")
    boat.change_part("Mât", "Aluminium")
    
    # Vérification que l'objet original est modifié
    print(f"\n3. Vérification de l'objet original 'mast':")
    print(f"   Contenu: {mast}")
    print(f"   Adresse mémoire: {id(mast)} (inchangée)")
    
    print(f"\n✓ L'objet Part a été modifié directement en mémoire!")
    print(f"  Les objets Python sont passés par référence.")
    print("="*50)


def main():
    """Fonction principale avec menu interactif"""
    
    # Création d'un bateau de course avec des pièces initiales
    initial_parts = [
        Part("Mât", "Bois"),
        Part("Coque", "Fibre de verre"),
        Part("Voile", "Nylon"),
        Part("Gouvernail", "Acier")
    ]
    
    ship = RacingShip("Speedster", initial_parts, max_speed=45.5)
    
    print("\n🚢 Bienvenue dans le système de gestion de bateau!")
    print(f"   Bateau créé: {ship.name}")
    
    while True:
        display_menu()
        choice = input("\nVotre choix: ").strip()
        
        if choice == "1":
            ship.display_state()
        
        elif choice == "2":
            print("\n--- Ajout de pièce ---")
            part_name = input("Nom de la pièce: ").strip()
            material = input("Matériau: ").strip()
            
            new_part = Part(part_name, material)
            ship.add_part(new_part)
        
        elif choice == "3":
            print("\n--- Remplacement de pièce ---")
            ship.display_state()
            part_name = input("Nom de la pièce à remplacer: ").strip()
            new_name = input("Nom de la nouvelle pièce: ").strip()
            new_material = input("Matériau de la nouvelle pièce: ").strip()
            
            new_part = Part(new_name, new_material)
            ship.replace_part(part_name, new_part)
        
        elif choice == "4":
            print("\n--- Modification de matériau ---")
            ship.display_state()
            part_name = input("Nom de la pièce à modifier: ").strip()
            new_material = input("Nouveau matériau: ").strip()
            
            ship.change_part(part_name, new_material)
        
        elif choice == "5":
            ship.display_history()
        
        elif choice == "6":
            demonstration_reference()
        
        elif choice == "7":
            print("\n👋 Merci d'avoir utilisé le système de gestion!")
            print(f"   État final du bateau '{ship.name}':")
            ship.display_state()
            break
        
        else:
            print("\n✗ Choix invalide. Veuillez réessayer.")
        
        input("\nAppuyez sur Entrée pour continuer...")


if __name__ == "__main__":
    main()