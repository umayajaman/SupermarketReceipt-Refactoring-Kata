import typing
from catalog import SupermarketCatalog

if typing.TYPE_CHECKING:
    from model_objects import Product


class FakeCatalog(SupermarketCatalog):
    def __init__(self):
        self.products = {}
        self.prices = {}

    def add_product(self, product, price):
        self.products[product.name] = product
        self.prices[product.name] = price

    def unit_price(self, product):
        return self.prices[product.name]

    def get_product(self, name: str) -> "Product":
        return self.products[name]
