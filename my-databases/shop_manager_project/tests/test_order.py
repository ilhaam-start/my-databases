from lib.order import *

"""
Testing the order constructs, customer name, item id and order date
"""
def test_order_construct():
    order = Order("name1", 32, "25/11/2023")
    assert order.customer_name == "name1"
    assert order.item_id == 32
    assert order.order_date == "25/11/2023"