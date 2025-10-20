import json
from models import authors

class Book:
    def __init__(self, id=None, title=None, publication_year=None, price=None, stock=None, author_id=None):
        self.id = id
        self.title = title
        self.publication_year = publication_year
        self.price = price
        self.stock = stock
        self.author_id = author_id

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    @classmethod
    def getAll(cls):
        database = open(r'src\data\books.json', 'r')
        result = []
        books = json.loads(database.read())
        for book in books:
            tmp = cls(book['id'], book['title'], book['publication_year'], book['price'], book['stock'], book['author_id'])
            aux = tmp.toJSON()
            result.append(json.loads(aux))
        return result

    @classmethod
    def getOne(cls, id):
        database = open(r'src\data\books.json', 'r')
        books = json.loads(database.read())
        for book in books:
            if book['id'] == id:
                return book
        return f'No book with id {id} exists in the database'

    @classmethod
    def create_book(cls, title, publication_year, price, stock, author_id):
        # Regla de negocio: Verificar si el autor existe
        author = authors.Author.getOne(author_id)
        if 'No author with id' in str(author):
            return "Cannot create book: Author with the given ID does not exist."

        database = open(r'src\data\books.json', 'r+')
        books = json.loads(database.read())
        new_book = {
            "id": len(books) + 1,
            "title": title,
            "publication_year": publication_year,
            "price": price,
            "stock": stock,
            "author_id": author_id
        }
        books.append(new_book)
        database.seek(0)
        json.dump(books, database, indent=4)
        return f"Created new book: {new_book}"

    @classmethod
    def update_book(cls, id, title, publication_year, price, stock, author_id):
        # Regla de negocio: Verificar si el autor existe
        author = authors.Author.getOne(author_id)
        if 'No author with id' in str(author):
            return "Cannot update book: Author with the given ID does not exist."

        database = open(r'src\data\books.json', 'r+')
        books = json.loads(database.read())
        updated_book = {}
        new_data = []
        for book in books:
            if book['id'] == id:
                updated_book = book
                book['title'] = title
                book['publication_year'] = publication_year
                book['price'] = price
                book['stock'] = stock
                book['author_id'] = author_id
            new_data.append(book)
        
        if updated_book:
            database.seek(0)
            database.truncate()
            json.dump(new_data, database, indent=4)
            return updated_book
        else:
            return 'No book exists with the given id'
    
    @classmethod
    def delete_book(cls, id):
        database = open(r'src\data\books.json', 'r+')
        books = json.loads(database.read())
        
        book_to_delete = None
        for book in books:
            if book['id'] == id:
                book_to_delete = book
                break
        
        if not book_to_delete:
            return f"Book with id {id} not found"

        books.remove(book_to_delete)

        # Re-indexar IDs
        for i, book in enumerate(books):
            book['id'] = i + 1

        database.seek(0)
        database.truncate()
        json.dump(books, database, indent=4)
        return f"Book with id {id} has been deleted."