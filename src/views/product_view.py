"""
Product view
"""
from models.product import Product
from controllers.product_controller import ProductController

class ProductView:
    @staticmethod
    def show_options():
        """ Show menu with operation options which can be selected by the user """
        controller = ProductController()
        while True:
            print("\n1. Montrer la liste de produits\n2. Ajouter un produit\n3. Modifier un produit\n4. Supprimer un produit\n5. Supprimer tous les produits\n6. Revenir au menu principal")
            choice = input("Choisissez une option: ")

            if choice == '1':
                products = controller.list_products()
                ProductView.show_products(products)
            elif choice == '2':
                name, brand, price = ProductView.get_inputs()
                product = Product(None, name, brand, price)
                controller.create_product(product)
            elif choice == '3':
                product_id = ProductView.get_id_input()
                name, brand, price = ProductView.get_inputs()
                product = Product(product_id, name, brand, price)
                controller.update_product(product)
            elif choice == '4':
                product_id = ProductView.get_id_input()
                controller.delete_product(product_id)
            elif choice == '5':
                controller.delete_all_products()
            elif choice == '6':
                controller.shutdown()
                break
            else:
                print("Cette option n'existe pas.")

    @staticmethod
    def show_products(products):
        """ List products """
        print("\n".join(f"{product.id}: {product.name} ({product.brand}) - {product.price}$" for product in products))

    @staticmethod
    def get_inputs():
        """ Prompt user for inputs necessary to add/edit a new product """
        name = input("Nom du produit : ").strip()
        brand = input("Marque du produit : ").strip()
        price = float(input("Prix du produit : ").strip())
        return name, brand, price

    @staticmethod
    def get_id_input():
        """ Prompt user for the ID of the product to edit/delete """
        product_id = input("ID du produit : ").strip()
        return product_id