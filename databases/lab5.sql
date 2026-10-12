-- Exercise 9
SELECT DISTINCT products.name
FROM orders
JOIN order_items ON order_items.order_id = orders.order_id
JOIN products ON products.product_id = order_items.product_id
WHERE orders.customer_id = 1;

-- Exercise 10
SELECT customers.email FROM customers WHERE customers.first_name = 'Erik';
UPDATE customers set email = 'erik.johansson@example.com' WHERE customers.first_name = 'Erik';

-- Exercise 11
CREATE VIEW customer_overview AS
SELECT c.customer_id, c.first_name, c.city, COUNT(o.order_id) AS number_of_orders
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id;

SELECT * FROM customer_overview;

-- Exercise 12
-- According to the GDPR data minimisation and storage limitation ideas, 
-- data should only be stored if needed and deleted when no longer needed. 
-- So if the new column with personal data (birth date) is added just in case, 
-- I do not think it should be added.