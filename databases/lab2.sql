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