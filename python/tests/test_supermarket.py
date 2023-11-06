import pytest

from shopping_cart import ShoppingCart


def test_no_discount(catalog, teller):
    apple = catalog.get_product("apple")
    potato = catalog.get_product("potato")

    cart = ShoppingCart()
    cart.add_item_quantity(apple, 2.5)
    cart.add_item_quantity(potato, 2)

    receipt = teller.checks_out_articles_from(cart)

    assert 10.955 == pytest.approx(receipt.total_price(), 0.01)
    assert [] == receipt.discounts
    assert 2 == len(receipt.items)

    assert apple == receipt.items[0].product
    assert 1.99 == receipt.items[0].price
    assert 2.5 * 1.99 == pytest.approx(receipt.items[0].total_price, 0.01)
    assert 2.5 == receipt.items[0].quantity

    assert potato == receipt.items[1].product
    assert 2.99 == receipt.items[1].price
    assert 2 * 2.99 == pytest.approx(receipt.items[1].total_price, 0.01)
    assert 2 == receipt.items[1].quantity


def test_ten_percent_discount(catalog, teller):
    apple = catalog.get_product("apple")
    toothbrush = catalog.get_product("toothbrush")

    cart = ShoppingCart()
    cart.add_item_quantity(apple, 2.5)
    cart.add_item_quantity(toothbrush, 2)

    receipt = teller.checks_out_articles_from(cart)

    assert 6.757 == pytest.approx(receipt.total_price(), 0.01)
    assert 1 == len(receipt.discounts)
    assert 2 == len(receipt.items)

    assert apple == receipt.items[0].product
    assert 1.99 == receipt.items[0].price
    assert 2.5 * 1.99 == pytest.approx(receipt.items[0].total_price, 0.01)
    assert 2.5 == receipt.items[0].quantity

    assert toothbrush == receipt.items[1].product
    assert 0.99 == receipt.items[1].price
    assert 2 * 0.99 == pytest.approx(receipt.items[1].total_price, 0.01)
    assert 2 == receipt.items[1].quantity

    discount_product = receipt.discounts[0]
    assert toothbrush == discount_product.product
    assert "10.0% off" == discount_product.description
    assert -0.198 == pytest.approx(discount_product.discount_amount, 0.01)


def test_two_for_amount(catalog, teller):
    shampoo = catalog.get_product("shampoo")
    flower = catalog.get_product("flower")

    cart = ShoppingCart()
    cart.add_item_quantity(shampoo, 4)
    cart.add_item_quantity(flower, 1)

    receipt = teller.checks_out_articles_from(cart)

    assert 3.27 == pytest.approx(receipt.total_price(), 0.01)
    assert 1 == len(receipt.discounts)
    assert 2 == len(receipt.items)

    assert shampoo == receipt.items[0].product
    assert 1.39 == receipt.items[0].price
    assert 4 * 1.39 == pytest.approx(receipt.items[0].total_price, 0.01)
    assert 4 == receipt.items[0].quantity

    assert flower == receipt.items[1].product
    assert 0.49 == receipt.items[1].price
    assert 0.49 == pytest.approx(receipt.items[1].total_price, 0.01)
    assert 1 == receipt.items[1].quantity

    assert shampoo == receipt.discounts[0].product
    assert "2 for 1.39" == receipt.discounts[0].description
    assert -2.78 == pytest.approx(receipt.discounts[0].discount_amount, 0.01)


def test_three_for_two(catalog, teller):
    pen = catalog.get_product("pen")
    milk = catalog.get_product("milk")

    cart = ShoppingCart()
    cart.add_item_quantity(pen, 4)
    cart.add_item_quantity(milk, 2)

    receipt = teller.checks_out_articles_from(cart)

    assert 8.95 == pytest.approx(receipt.total_price(), 0.01)
    assert 1 == len(receipt.discounts)
    assert 2 == len(receipt.items)

    assert pen == receipt.items[0].product
    assert 1.99 == receipt.items[0].price
    assert 4 * 1.99 == pytest.approx(receipt.items[0].total_price, 0.01)
    assert 4 == receipt.items[0].quantity

    assert milk == receipt.items[1].product
    assert 1.49 == receipt.items[1].price
    assert 2 * 1.49 == pytest.approx(receipt.items[1].total_price, 0.01)
    assert 2 == receipt.items[1].quantity

    assert pen == receipt.discounts[0].product
    assert "3 for 2" == receipt.discounts[0].description
    assert -1.99 == pytest.approx(receipt.discounts[0].discount_amount, 0.01)


def test_five_for_two(catalog, teller):
    pencil = catalog.get_product("pencil")
    eraser = catalog.get_product("eraser")

    cart = ShoppingCart()
    cart.add_item_quantity(pencil, 7)
    cart.add_item_quantity(eraser, 1)

    receipt = teller.checks_out_articles_from(cart)

    assert 2.67 == pytest.approx(receipt.total_price(), 0.01)
    assert 1 == len(receipt.discounts)
    assert 2 == len(receipt.items)

    assert pencil == receipt.items[0].product
    assert 0.69 == receipt.items[0].price
    assert 7 * 0.69 == pytest.approx(receipt.items[0].total_price, 0.01)
    assert 7 == receipt.items[0].quantity

    assert eraser == receipt.items[1].product
    assert 0.59 == receipt.items[1].price
    assert 0.59 == pytest.approx(receipt.items[1].total_price, 0.01)
    assert 1 == receipt.items[1].quantity

    assert pencil == receipt.discounts[0].product
    assert "5 for 0.69" == receipt.discounts[0].description
    assert -2.76 == pytest.approx(receipt.discounts[0].discount_amount, 0.01)


def test_add_item_multiple_times(catalog, teller):
    shampoo = catalog.get_product("shampoo")

    cart = ShoppingCart()
    cart.add_item(shampoo)
    cart.add_item(shampoo)

    receipt = teller.checks_out_articles_from(cart)

    assert 1.39 == pytest.approx(receipt.total_price(), 0.01)
    assert 1 == len(receipt.discounts)
    assert 2 == len(receipt.items)

    assert shampoo == receipt.items[0].product
    assert 1.39 == receipt.items[0].price
    assert 1.39 == pytest.approx(receipt.items[0].total_price, 0.01)
    assert 1 == receipt.items[0].quantity

    assert shampoo == receipt.discounts[0].product
    assert "2 for 1.39" == receipt.discounts[0].description
    assert -1.39 == pytest.approx(receipt.discounts[0].discount_amount, 0.01)