import sqlite3

db = sqlite3.connect("books-collection.db")  # Now create a connection to a new database
cursor = db.cursor()  # cursor is also known as the mouse or pointer

# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")

db.commit()