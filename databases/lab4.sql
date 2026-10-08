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
