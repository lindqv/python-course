SELECT first_name, email FROM customers;
SELECT * FROM products WHERE category = 'Shoes';
SELECT * FROM customers WHERE city = 'Uppsala';
SELECT name, price FROM products where price = 199;
SELECT * FROM products ORDER BY name;
SELECT * FROM customers ORDER BY joined_date;
SELECT * FROM products WHERE stock = 0;
SELECT * FROM customers WHERE city in ('Stockholm', 'Göteborg');
SELECT name AS product, price AS price_sek from products;

SELECT * FROM products WHERE category in ('Clothing', 'Shoes') AND price > 1000;
SELECT name, price, stock, price * stock AS stock_value FROM products WHERE stock > 0;
SELECT first_name FROM customers WHERE first_name LIKE '____';
SELECT * FROM products ORDER BY price LIMIT 5 OFFSET 5;
SELECT * FROM customers WHERE joined_date < '2025-01-01' AND city != 'Uppsala' ORDER BY city, last_name;

SELECT * FROM products WHERE category != 'Accessories' AND stock > 0 AND name LIKE '% %' ORDER BY category, price DESC;
SELECT * FROM customers WHERE city LIKE 'S%' OR city LIKE 'M%' OR city IS NULL;
SELECT * FROM products WHERE category = 'Shoes' ORDER BY price DESC LIMIT 1 OFFSET 1;
SELECT * FROM customers ORDER BY joined_date DESC LIMIT 3;