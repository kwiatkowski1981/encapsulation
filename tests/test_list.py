from basket.List import List
from basket.ListItem import ListItem
from basket.Product import Product


def test_add_item_to_list_once():
    # given
    product = Product('Chleb', 4.30)
    to_buy = List()

    # when
    to_buy.add_item(product, 3)

    # then
    assert to_buy.calculate_total_cost() == 4.30 * 3
    assert len(to_buy.list_items()) == 1


def test_add_the_same_item_to_the_list_twice():
    # given
    product = Product('Chleb', 4.30)
    to_buy = List()

    # when
    to_buy.add_item(product, 3)
    to_buy.add_item(product, 2)

    # then
    assert to_buy.calculate_total_cost() == 21.5
    assert len(to_buy.list_items()) == 1


def test_add_to_different_products_to_list():
    # given
    product = Product('Chleb', 4.30)
    product2 = Product('Masło', 6)
    to_buy = List()

    # when
    to_buy.add_item(product, 3)
    to_buy.add_item(product2, 3)

    # then
    assert to_buy.calculate_total_cost() == 30.9
    assert len(to_buy.list_items()) == 2
