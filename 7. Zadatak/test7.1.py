"""
Given the following data definition, select the name of all authors whose name starts with letter "N", and who've published more than 30 books or are under 30 years old.

Code: 

TABLE authors, name VARCHAR(30) NOT NULL PRIMARY KEY, books INTEGER NOT NULL, age INTEGER NOT NULL.

Example case: 

CRATE TABLE authors (name VARCHAR(30) NOT NULL PRIMARY KEY, books INTEGER NOT NULL, age INTEGER NOT NULL);
INSERT INTO authors (name,books,age) values ("Mia",40,25); 
INSERT INTO authors (name,books,age) values("Neo", 35,35);
INSERT INTO authors (name,books,age) values("Nolan", 40,25);

Expected output (in any order): name, , Neo,Nolan.

Explanation: In this example, Neo has has published more than 30 books, while Nolan is under 30 years old. Both names start with letter "N".

"""

# RJEŠENJE:

# SELECT name 
# FROM authors 
# WHERE name LIKE 'N%' 
# AND (books > 30 OR age < 30);

"""

Explanation:  name LIKE 'N%'
                 This filters for authors whose names start with the letter "N",
              (books > 30 OR age < 30): This checks if the author has either published more than 30 books or is under 30 years old.
             
OUTPUT:

name
_____
Neo
Nolan

"""