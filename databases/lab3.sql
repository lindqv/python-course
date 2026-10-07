SELECT COUNT (*) FROM orders;

INSERT INTO customers (customer_id, first_name, last_name, email, city, joined_date)
VALUES (11, 'Sanne', 'Lindqvist', 's.lindqvist@example.com', 'Stockholm', '2026-10-07'); 
SELECT * FROM customers;

INSERT INTO products (name, category, price, stock) VALUES ('Scarf', 'Accessories', 229, 15);
INSERT INTO products (name, category, price, stock) VALUES ('Gloves', 'Accessories', 199, 20);
SELECT * FROM products;

INSERT INTO orders (customer_id, order_date, status) VALUES (7, '2026-10-07', 'new');
INSERT INTO order_items (order_id, customer_id, order_date, status) VALUES (16, 7, '2026-10-07', 'new');
INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES (16, 10, 2, 179);
SELECT * FROM orders;
SELECT * FROM order_items;

-- This will fail due to quantity being 0. CHECK constraint failed: quantity > 0
-- INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES (17, 1, 0, 599);

SELECT * FROM orders WHERE order_id = 12;
UPDATE orders SET status = 'shipped' WHERE order_id = 12;

SELECT * FROM products WHERE product_id = 5;
UPDATE products SET stock = 50 WHERE product_id = 5;
SELECT * FROM products;

SELECT * FROM products WHERE category = 'Accessories';
UPDATE products SET price = price * 1.10 WHERE category = 'Accessories';

SELECT * FROM orders;
SELECT * FROM orders WHERE status = 'cancelled';
SELECT * FROM orders WHERE order_id = 7;
SELECT * FROM order_items WHERE order_id = 7;
DELETE FROM order_items WHERE order_id = 7;
DELETE FROM orders WHERE order_id = 7;

-- Trying to delete the order without deleting the items first causes a FOREIGN KEY constraint failed error.

SELECT COUNT(*) FROM orders;