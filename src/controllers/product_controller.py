"""
Product controller
"""

from daos.product_dao import ProductDAO

class ProductController:
    def __init__(self):
        self.dao = ProductDAO()

    def list_products(self):
        """ List all products """
        return self.dao.select_all()

    def create_product(self, product):
        """ Create a new product based on product inputs """
        self.dao.insert(product)

    def shutdown(self):
        """ Close database connection """
        self.dao.close()

    def update_product(self, product):
        """ Update an existing product """
        self.dao.update(product)

    def delete_product(self, product_id):
        """ Delete a product by its ID """
        self.dao.delete(product_id)

    def delete_all_products(self): #optional
        """ Delete all products """
        self.dao.delete_all()