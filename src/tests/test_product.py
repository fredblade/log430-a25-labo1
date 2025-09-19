from daos.product_dao import ProductDAO
from models.product import Product

dao = ProductDAO()

def test_product_select():
    dao.delete_all()
    product = Product(None, "Test Product1", "Test Brand", 1.99)
    dao.insert(product)
    product = Product(None, "TesProduct2", "TeBrand", 9.99)
    dao.insert(product)
    product = Product(None, "corn", "Brand", 9.99)
    dao.insert(product)

    product_list = dao.select_all()
    assert len(product_list) >= 3
    dao.delete_all()

def test_product_insert():
    product = Product(None, "new product", "business", 19.59)
    dao.insert(product)
    product_list = dao.select_all()
    names = [p.name for p in product_list]
    assert product.name in names

def test_product_update():
    product = Product(None, "Old Product", "Old Brand", 119.99)
    assigned_id = dao.insert(product)

    corrected_name = "Updated Product"
    product.id = assigned_id
    product.name = corrected_name

    dao.update(product)

    product_list = dao.select_all()
    names = [p.name for p in product_list]
    assert corrected_name in names

def test_product_delete():
    product = Product(None, name="Test Product", brand="Test Brand", price=9.99)
    product_id = dao.insert(product)

    product_list = dao.select_all()
    names = [p.name for p in product_list]
    assert product.name in names

    dao.delete(product_id)

    product_list = dao.select_all()
    names = [p.name for p in product_list]
    assert product.name not in names