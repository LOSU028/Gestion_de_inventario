from flask import jsonify

def display_authors(authors):
    print ('Authors in the database: ', len(authors))
    for author in authors:
        print (author)
    return 'OK'

def display_author(author, id):
    print ('Author with id: ', id)
    print(author)
    return 'OK'

def display_updated_author(id,author):
    print('Author with id:', id, "has been updated:")
    print(author)
    return 'OK'

def display_deleted_author(id):
    print('Author with id: ', id, 'has been deleted')
    return 'OK'

# Vistas para Libros 

def display_books(books):
    print('Books in the database: ', len(books))
    for book in books:
        print(book)
    return 'OK'

def display_book(book, id):
    print('Book with id: ', id)
    print(book)
    return 'OK'

def display_updated_book(id, book):
    print('Book with id:', id, "has been updated:")
    print(book)
    return 'OK'

def display_deleted_message(message):
    print(message)
    return 'OK'