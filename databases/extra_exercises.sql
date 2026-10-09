-- Level 1
SELECT * FROM products 
WHERE category IN ('Clothing', 'Accessories') AND price BETWEEN 150 AND 500
ORDER BY price DESC;

SELECT * FROM orders WHERE order_date LIKE '2026-02-%' AND status != 'cancelled';

SELECT o.order_id, p.name, oi.quantity, oi.quantity * oi.unit_price AS line_total 
FROM orders o
JOIN order_items oi ON oi.order_id = o.order_id
JOIN products p ON p.product_id = oi.product_id
WHERE line_total > 500
ORDER BY line_total DESC;

SELECT DISTINCT customers.customer_id, customers.first_name, customers.last_name, customers.city
FROM orders
LEFT JOIN customers ON customers.customer_id = orders.customer_id
WHERE city IN ('Uppsala', 'Stockholm');