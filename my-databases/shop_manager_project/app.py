from lib.database_connection import *
import lib.shop_item as shop_items
import lib.order as orders

def main():
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("seeds/shop_manager_project.sql")

    print("Welcome to the shop management program!")
    while True:
        print("\nWhat do you want to do?")
        print("1 = list all shop items")
        print("2 = create a new item")
        print("3 = list all orders")
        print("4 = create a new order")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            items = shop_items.list_shop_items(connection)
            if items:
                for item in items:
                    print("#{} {} - Unit price: {} - Quantity: {}".format(item[0], item[1], item[2], item[3]))
            else: 
                print("No items founds in the shop")
        elif choice == "2":
            shop_items.create_shop_item(connection)
        elif choice == "3":
            orders_list = orders.list_order(connection)
            for order in orders_list:
                print("#{} - Customer: {} - Item: {} - Order Date: {}".format(order[0], order[1], order[5], order[3]))
        elif choice == "4":
            orders.create_order(connection)
        else:
            print("Invalid choice. Please try again.")
    
    connection.close()

if __name__ == "__main__":
    main()