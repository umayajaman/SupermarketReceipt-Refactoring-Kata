import typing


if typing.TYPE_CHECKING:
    from model_objects import Discount, Product, ProductQuantity


class ReceiptItem:
    def __init__(self, product: "Product",
                 quantity: "ProductQuantity",
                 price: float,
                 total_price: float):
        self.product = product
        self.quantity = quantity
        self.price = price
        self.total_price = total_price


class Receipt:
    def __init__(self):
        self._items = []
        self._discounts = []

    def total_price(self) -> float:
        total = 0
        for item in self.items:
            total += item.total_price
        for discount in self.discounts:
            total += discount.discount_amount
        return total

    def add_product(
            self, product: "Product",
            quantity: "ProductQuantity",
            price: float,
            total_price: float):
        self._items.append(ReceiptItem(product, quantity, price, total_price))

    def add_discount(self, discount: "Discount"):
        self._discounts.append(discount)

    @property
    def items(self):
        return self._items[:]

    @property
    def discounts(self):
        return self._discounts[:]
