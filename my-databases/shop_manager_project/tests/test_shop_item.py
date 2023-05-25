from lib.shop_item import *

"""
Testing the shop item constructs, name, unit price and quantiy
"""
def test_item_construct():
    shop_item = ShopItem("item1", 3.00, 25)
    assert shop_item.name == "item1"
    assert shop_item.unit_price == 3.00
    assert shop_item.quantity == 25