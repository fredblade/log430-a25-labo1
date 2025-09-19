"""
Store manager application
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
from views.user_view import UserView
from views.product_view import ProductView

def show_mainmenu():
    """ Show main menu to choose between user and product management """
    while True:
        print("\n===== LE MAGASIN DU COIN =====")
        print("1. Gestion des utilisateurs")
        print("2. Gestion des produits")
        print("3. Quitter l'application")
        
        choice = input("Choisissez une option: ").strip()
        
        if choice == '1':
            print("\n--- GESTION DES UTILISATEURS ---")
            UserView.show_options()
        elif choice == '2':
            print("\n--- GESTION DES PRODUITS ---")
            ProductView.show_options()
        elif choice == '3':
            print("Au revoir!")
            break
        else:
            print("Cette option n'existe pas.")

if __name__ == '__main__':
    show_mainmenu()
