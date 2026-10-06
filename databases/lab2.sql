-- Exercise 1-4
CREATE TABLE books (
	book_id INTEGER PRIMARY KEY,
	title TEXT NOT NULL,
	author TEXT,
	year INTEGER CHECK(year > 1400)
);

ALTER TABLE books ADD COLUMN isbn TEXT;

SELECT * FROM books;

DROP TABLE books;

-- Exercise 5-7
CREATE TABLE reviews (
	review_id INTEGER NOT NULL PRIMARY KEY,
	rating INTEGER CHECK(rating BETWEEN 1 AND 5),
	comment TEXT,
	product_id INTEGER NOT NULL,
	FOREIGN KEY(product_id) REFERENCES products(product_id)
);

-- Adding a review with rating 6 causes an error due to the CHECK constraint failing.
INSERT INTO reviews (review_id, rating, comment, product_id) 
VALUES (1, 6, "Excellent", 1);

-- However a review with rating 5 can be added.
INSERT INTO reviews (review_id, rating, comment, product_id) 
VALUES (1, 5, "Excellent", 1);

SELECT * FROM reviews;

-- Adding a review for product with id 50 causes an error, FOREIGN KEY constraint failed.
INSERT INTO reviews (review_id, rating, comment, product_id) 
VALUES (2, 5, "Excellent", 50);


-- Extra challenges level 1
CREATE TABLE suppliers (
	supplier_id INTEGER NOT NULL PRIMARY KEY,
	name NOT NULL UNIQUE,
	country TEXT DEFAULT 'Sweden',
	email TEXT
);

INSERT INTO suppliers (supplier_id, name, email) VALUES (1, "Test supplier", "test@example.com");
SELECT * FROM suppliers;
-- The country column says 'Sweden' for this newly added supplier.

INSERT INTO suppliers (supplier_id, name, email) VALUES (2, "Nordic Textiles", "nordic.textiles@example.com");
INSERT INTO suppliers (supplier_id, name, email) VALUES (3, "Nordic Textiles", "nordic.textiles@example.com");
-- The line above causes an error: UNIQUE constraint failed: suppliers.name. 
-- Adding another supplier with the same name was stopped by the UNIQUE constraint for name.

CREATE TABLE coupons (
	code TEXT NOT NULL PRIMARY KEY,
	discount_percent INTEGER NOT NULL CHECK(discount_percent BETWEEN 1 AND 90),
	valid_until TEXT NOT NULL
);

-- This gives a CHECK constraint failed error.
INSERT INTO coupons (code, discount_percent, valid_until) VALUES ('SUMMER20', 95, '2026-10-31')
-- The line below works.
INSERT INTO coupons (code, discount_percent, valid_until) VALUES ('SUMMER20', 20, '2026-10-31')


-- Extra challenges level 2

-- This supplier gets id 3. 
-- If an integer primary key is not given a value it will be automatically filled with an unused integer.
-- This is usually one more than the current largest ROWID in use.
INSERT INTO suppliers (name) VALUES ("Global Textiles");
SELECT * FROM suppliers;

ALTER TABLE suppliers RENAME COLUMN email TO contact_email;
SELECT * FROM suppliers;

PRAGMA table_info(products);


CREATE TABLE product_suppliers (
	purchase_price REAL CHECK(purchase_price > 0),
	product_id INTEGER NOT NULL,
	supplier_id INTEGER NOT NULL,
	FOREIGN KEY (product_id) REFERENCES products(product_id),
	FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id),
	PRIMARY KEY (product_id, supplier_id)
);

INSERT INTO product_suppliers (purchase_price, product_id, supplier_id) VALUES (100, 1, 99);


CREATE TABLE campaigns (
	name TEXT,
	start_date TEXT,
	end_date TEXT CHECK(end_date > start_date)
);

INSERT INTO campaigns (name, start_date, end_date) VALUES ('New campaign', '2026-10-06', '2026-10-01');