"""
Placeholder for the fixtures
"""

import pytest

from model_objects import Product, ProductUnit, SpecialOfferType
from teller import Teller
from tests.fake_catalog import FakeCatalog


@pytest.fixture
def catalog():
    catalog = FakeCatalog()

    # product 1
    toothbrush = Product("toothbrush", ProductUnit.EACH)
    catalog.add_product(toothbrush, 0.99)

    # product 2
    apple = Product("apple", ProductUnit.KILO)
    catalog.add_product(apple, 1.99)

    # product 3
    milk = Product("milk", ProductUnit.EACH)
    catalog.add_product(milk, 1.49)

    # product 4
    potato = Product("potato", ProductUnit.KILO)
    catalog.add_product(potato, 2.99)

    # product 5
    shampoo = Product("shampoo", ProductUnit.EACH)
    catalog.add_product(shampoo, 1.39)

    # product 6
    pen = Product("pen", ProductUnit.EACH)
    catalog.add_product(pen, 1.99)

    # product 7
    flower = Product("flower", ProductUnit.EACH)
    catalog.add_product(flower, 0.49)

    # product 8
    pencil = Product("pencil", ProductUnit.EACH)
    catalog.add_product(pencil, 0.69)

    # product 9
    eraser = Product("eraser", ProductUnit.EACH)
    catalog.add_product(eraser, 0.59)

    return catalog


@pytest.fixture
def teller(catalog):
    teller = Teller(catalog)
    toothbrush = catalog.get_product("toothbrush")
    shampoo = catalog.get_product("shampoo")
    flower = catalog.get_product("flower")
    pen = catalog.get_product("pen")
    milk = catalog.get_product("milk")
    pencil = catalog.get_product("pencil")
    eraser = catalog.get_product("eraser")
    teller.add_special_offer(SpecialOfferType.TEN_PERCENT_DISCOUNT, toothbrush, 10.0)
    teller.add_special_offer(SpecialOfferType.TWO_FOR_AMOUNT, shampoo, catalog.unit_price(shampoo))
    teller.add_special_offer(SpecialOfferType.TWO_FOR_AMOUNT, flower, catalog.unit_price(flower))
    teller.add_special_offer(SpecialOfferType.THREE_FOR_TWO, pen, catalog.unit_price(pen))
    teller.add_special_offer(SpecialOfferType.THREE_FOR_TWO, milk, catalog.unit_price(milk))
    teller.add_special_offer(SpecialOfferType.FIVE_FOR_AMOUNT, pencil, catalog.unit_price(pencil))
    teller.add_special_offer(SpecialOfferType.FIVE_FOR_AMOUNT, eraser, catalog.unit_price(eraser))

    return teller
