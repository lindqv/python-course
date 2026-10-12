-- Lab 1, questions 1-10
SELECT first_name, email FROM customers;
SELECT * FROM products WHERE category = 'Shoes';
SELECT * FROM customers WHERE city = 'Uppsala';
SELECT name, price FROM products WHERE price = 199;
SELECT * FROM products ORDER BY name;
SELECT * FROM customers ORDER BY joined_date;
SELECT * FROM products WHERE stock = 0;
SELECT * FROM customers ORDER BY joined_date DESC LIMIT 3;
SELECT * FROM customers WHERE city IN ('Stockholm', 'Göteborg');
SELECT name AS product, price AS price_sek from products;

-- Bonus questions
SELECT * FROM products WHERE category IN ('Clothing', 'Shoes') AND price > 1000;
SELECT name, price, stock, price * stock AS stock_value FROM products WHERE stock > 0;
SELECT first_name FROM customers WHERE first_name LIKE '____';
SELECT * FROM products ORDER BY price LIMIT 5 OFFSET 5;
SELECT * FROM customers WHERE joined_date < '2025-01-01' AND city != 'Uppsala' ORDER BY city, last_name;

-- Challenge questions level 1
SELECT * FROM products WHERE category != 'Accessories' AND stock > 0 AND name LIKE '% %' ORDER BY category, price DESC;
SELECT * FROM customers WHERE city LIKE 'S%' OR city LIKE 'M%' OR city IS NULL;
SELECT * FROM products WHERE category = 'Shoes' ORDER BY price DESC LIMIT 1 OFFSET 1;
SELECT * FROM customers WHERE joined_date LIKE '2024%' OR joined_date LIKE '2025%' ORDER BY joined_date DESC LIMIT 3;

-- Challenge questions level 2
SELECT first_name || ' ' || last_name AS full_name FROM customers;

SELECT *,
CASE
	WHEN price < 200 THEN 'budget'
	WHEN price <= 799 THEN 'mid'
	WHEN price > 799 THEN 'premium'
END AS price_level
FROM products;

SELECT COALESCE(first_name, 'Unknown'), COALESCE(city, 'Unknown') FROM customers;

SELECT *, strftime('%m', joined_date) AS month FROM customers 
where month IN ('01', '02', '03', '04', '05', '06');

SELECT * FROM products ORDER BY LENGTH(name) DESC LIMIT 1;

SELECT email, substr(email, 1, instr(email, '@') - 1) AS username FROM customers;

-- Challenge questions level 3
SELECT * FROM products WHERE price > (SELECT AVG(price) from products);

SELECT *, name || " costs " || ROUND(price) || " kr" AS price_description FROM products;
SELECT *, name || " costs " || CAST(price AS INT) || " kr" AS price_description FROM products;

SELECT city, COUNT(customer_id) AS customer_count FROM customers GROUP BY city ORDER BY customer_count DESC;
