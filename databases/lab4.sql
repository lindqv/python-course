SELECT customers.first_name, customers.last_name, orders.status 
FROM customers 
JOIN orders ON orders.customer_id = customers.customer_id;

SELECT customers.first_name, orders.order_id, orders.status 
FROM customers 
JOIN orders ON orders.customer_id = customers.customer_id
WHERE customers.first_name = 'Erik';

SELECT customers.city, customers.first_name, orders.order_id, orders.status, orders.order_date
FROM customers 
JOIN orders ON orders.customer_id = customers.customer_id
WHERE customers.city = 'Göteborg'
ORDER BY orders.order_date DESC;

SELECT products.name, products.category, order_items.order_id
FROM products
JOIN order_items ON order_items.product_id = products.product_id;

SELECT products.name, products.category, order_items.order_id
FROM products
JOIN order_items ON order_items.product_id = products.product_id
WHERE products.category = 'Shoes';

SELECT p.name, oi.quantity, oi.unit_price, oi.quantity * oi.unit_price AS line_total
FROM products p
JOIN order_items oi ON oi.product_id = p.product_id
WHERE oi.order_id = 10;

SELECT customers.first_name, orders.order_date, products.name
FROM orders
JOIN customers ON customers.customer_id = orders.customer_id
JOIN order_items ON order_items.order_id = orders.order_id
JOIN products ON products.product_id = order_items.product_id
WHERE products.name = 'Hoodie Black';

SELECT customers.first_name, orders.order_date, products.name
FROM order_items
JOIN orders ON orders.order_id = order_items.order_id
JOIN products ON products.product_id = order_items.product_id
JOIN customers ON customers.customer_id = orders.customer_id
WHERE products.name = 'Hoodie Black';

SELECT * 
FROM customers
LEFT JOIN orders ON orders.customer_id = customers.customer_id;

SELECT * 
FROM products
LEFT JOIN order_items ON order_items.product_id = products.product_id
WHERE order_id IS NULL;

SELECT customers.first_name, products.name AS product_name, order_items.quantity, customers.city
FROM customers
JOIN orders ON orders.customer_id = customers.customer_id 
JOIN order_items ON order_items.order_id = orders.order_id
JOIN products ON products.product_id = order_items.product_id
WHERE customers.city = 'Uppsala'
ORDER BY customers.first_name;