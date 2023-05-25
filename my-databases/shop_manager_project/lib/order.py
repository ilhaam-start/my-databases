class Order:
    def __init__(self, customer_name, item_id, order_date):
        self.customer_name = customer_name
        self.item_id = item_id
        self.order_date = order_date

    def save(self, db_connection):
        query = "INSERT INTO orders (customer_name, item_id, order_date) VALUES (?, ?, ?)"
        parameters = (self.customer_name, self.item_id, self.order_date)
        db_connection.execute(query, parameters)

def list_orders(db_connection):
    query = "SELECT orders.*, shop_items.name FROM orders INNER JOIN shop_items ON orders.item_id = shop_items.id"
    return db_connection.execute(query)

def create_order(db_connection):
    customer_name = input("Enter the customer name: ")
    item_id = int(input("Enter the item ID: "))
    order_date = input("Enter the order date: ")
    order = Order(customer_name, item_id, order_date)
    order.save(db_connection)