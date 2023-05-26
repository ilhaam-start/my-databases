class ShopItem:
    def __init__(self, name, unit_price, quantity):
        self.name = name
        self.unit_price = unit_price
        self.quantity = quantity

    def save(self, db_connection):
        query = "INSERT INTO shop_items (name, unit_price, quantity) VALUES (%s, %s, %s)"
        parameters = (self.name, self.unit_price, self.quantity)
        db_connection.execute(query, parameters)

def list_shop_items(db_connection):
    query = "SELECT id, name, unit_price, quantity FROM shop_items"
    items = db_connection.execute(query)
    return [tuple(item.values()) for item in items]

def create_shop_item(db_connection):
    name = input("Enter the item name: ")
    unit_price = float(input("Enter the unit price: "))
    quantity = int(input("Enter the quantity: "))
    item = ShopItem(name, unit_price, quantity)
    item.save(db_connection)