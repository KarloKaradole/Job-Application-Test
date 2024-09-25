CREATE TABLE users (id INTEGER PRIMARY KEY NOT NULL, email VARCHAR(50) NOT NULL, passwordHash VARCHAR(60) NOT NULL);
INSERT INTO users(id, email, passwordHash) VALUES (1, "mike@acme.com","12345678");
INSERT INTO users(id,email,passwordHash) VALUES (2, "steve@acme.com", "87654321");

SOLUTION:

ALTER TABLE users 
ADD COLUMN banned INTEGER DEFAULT 0 CHECK (banned IN (0, 1))
SELECT * FROM users;


/*Explanation:  ALTER TABLE users ADD COLUMN banned INTEGER DEFAULT 0; -> Adds a new column banned to the users table. Since no values are provided initially, the default value 0 will be applied to existing records.
                SELECT * FROM users; -> Retrieves all records, including the new banned column, where its default value is 0.





