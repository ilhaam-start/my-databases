from lib.book import *

"""
A book construct with id, title, and author name
"""
def test_book_construct():
    book = Book(1, "Nineteen Eighty-Four", "George Orwell")
    assert book.id == 1
    assert book.title == "Nineteen Eighty-Four"
    assert book.author_name == "George Orwell"

"""
Test the format as string
"""
def test_format_as_string():
    book = Book(1, "Nineteen Eighty-Four", "George Orwell")
    assert str(book) == "1 - Nineteen Eighty-Four - George Orwell"