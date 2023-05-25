DROP TABLE IF EXISTS orders;
DROP SEQUENCE IF EXISTS orders_id_seq;

DROP TABLE IF EXISTS shop_items;
DROP SEQUENCE IF EXISTS shop_items_id_seq;

CREATE SEQUENCE IF NOT EXISTS shop_items_id_seq;
CREATE TABLE shop_items (
    id SERIAL PRIMARY KEY,
    name text,
    unit_price real,
    quantity int
);

CREATE SEQUENCE IF NOT EXISTS orders_id_seq;
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_name text,
    item_id int,
    order_date text,
    foreign key(item_id) references shop_items(id) on delete cascade
);

INSERT INTO shop_items (name, unit_price, quantity) VALUES ('Super Shark Vacuum Cleaner', 99, 30);
INSERT INTO shop_items (name, unit_price, quantity) VALUES ('Makerspresso Coffee Machine', 69, 15);
INSERT INTO shop_items (name, unit_price, quantity) VALUES ('IKEA wardrobe', 129, 2);

INSERT INTO orders (customer_name, item_id, order_date) VALUES ('Ilhaam', 1, '2023-05-01');
INSERT INTO orders (customer_name, item_id, order_date) VALUES ('name2', 2, '2023-05-20');
