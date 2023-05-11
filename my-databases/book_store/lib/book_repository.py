from lib.book import *

class BookRepository:

    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM books')
        books = []
        for row in rows:
            item = Book(row["id"], row["title"], row["author_name"])
            books.append(item)
        return books
    
    def find(self, book_id):
        rows = self._connection.execute('SELECT * FROM books WHERE id = %s', [book_id])
        row = rows[0]
        item = Book(row["id"], row["title"], row["author_name"])
        return item
    
    def create(self, title, author_name):
        self._connection.execute('INSERT INTO books (title, author_name) VALUES (%s, %s)', [title, author_name])
        return None
    
    def update(self, book_id, new_title, _new_author):
        self._connection.execute('UPDATE books SET title = %s, author_name = %s WHERE id = %s', [new_title, _new_author, book_id])
        return None
    
    def delete(self, book_id):
        self._connection.execute('DELETE FROM books WHERE id = %s', [book_id])
        return None
