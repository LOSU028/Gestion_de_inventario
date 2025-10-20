import sys
sys.path.insert(0,"../models")

from models import books
from views import views

def list_books():
    books_in_db = books.Book.getAll()
    return views.display_books(books_in_db)

def get_book_by_id(id):
    book = books.Book.getOne(id)
    return views.display_book(book, id)

def create_book(data):
    title = data.get("title")
    publication_year = data.get("publication_year")
    price = data.get("price")
    stock = data.get("stock")
    author_id = data.get("author_id")
    result = books.Book.create_book(title, publication_year, price, stock, author_id)
    return result

def update_book(id, data):
    title = data.get("title")
    publication_year = data.get("publication_year")
    price = data.get("price")
    stock = data.get("stock")
    author_id = data.get("author_id")
    updated_book = books.Book.update_book(id, title, publication_year, price, stock, author_id)
    return views.display_updated_book(id, updated_book)

def delete_book(id):
    result = books.Book.delete_book(id)
    return views.display_deleted_message(result)