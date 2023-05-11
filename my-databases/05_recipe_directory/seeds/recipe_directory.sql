DROP TABLE recipes;

CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    name text,
    cooking_time int,
    rating int
);

INSERT INTO recipes (name, cooking_time, rating) VALUES ('Lasagna', 60, 5);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Trifle', 30, 1);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Jollof Rice', 60, 5);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Chocolate Oreo Cake', 80, 4);