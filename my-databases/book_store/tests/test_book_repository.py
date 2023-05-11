from lib.book_repository import *
from lib.book import *

"""
when #all is called, this gets all the books back in a list
"""
def test_get_all_records(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repo = BookRepository(db_connection)
    books = repo.all()
    assert [str(book) for book in books] == [
        "1 - Nineteen Eighty-Four - George Orwell",
        "2 - Mrs Dalloway - Virginia Woolf",
        "3 - Emma - Jane Austen",
        "4 - Dracula - Bram Stoker",
        "5 - The Age of Innocence - Edith Wharton"
    ]

"""
when #find is called using the id this returns the book id, name and author
"""
def test_find_id_get_book_details(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repo = BookRepository(db_connection)
    books = repo.find(2)
    assert str(books) == "2 - Mrs Dalloway - Virginia Woolf"

"""
Test when new book created by calling #create, the new book is
added to the list when #all is called
"""
def test_create_new_book_return_in_list(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repo = BookRepository(db_connection)
    repo.create("Stormbreaker", "Anthony Horowitz")
    books = repo.all()
    assert [str(book) for book in books] == [
        "1 - Nineteen Eighty-Four - George Orwell",
        "2 - Mrs Dalloway - Virginia Woolf",
        "3 - Emma - Jane Austen",
        "4 - Dracula - Bram Stoker",
        "5 - The Age of Innocence - Edith Wharton",
        "6 - Stormbreaker - Anthony Horowitz"
    ]

"""
when the #update method is called, this updates the title 
and author name
"""
def test_details_updated_in_list(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repo = BookRepository(db_connection)
    repo.update(1, "Point Blanc", "Anthony Horowitz")
    books = repo.find(1)
    assert str(books) == "1 - Point Blanc - Anthony Horowitz"

"""
When #delete is called this should remove the book from the list
"""
def test_delete_book_shorten_list(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repo = BookRepository(db_connection)
    repo.delete(3)
    books = repo.all()
    assert [str(book) for book in books] == [
        "1 - Nineteen Eighty-Four - George Orwell",
        "2 - Mrs Dalloway - Virginia Woolf",
        "4 - Dracula - Bram Stoker",
        "5 - The Age of Innocence - Edith Wharton"
    ]