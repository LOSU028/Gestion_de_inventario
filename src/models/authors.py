
import json
class Author:
    def __init__(self, id = None, name = None, last_name = None, nationality = None):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.nationality = nationality

    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__, 
            sort_keys=True,
            indent=4)

    @classmethod
    def getAll(self):
        database = open(r'src\data\authors.json', 'r')
        result = []
        authors = json.loads(database.read())
        for author in authors:
            tmp = Author(author['id'],author['name'], author['last_name'], author['nationality'])
            aux = tmp.toJSON()
            result.append(json.loads(aux))
        return result
    
    @classmethod
    def getOne(self,id):
        database = open(r'src\data\authors.json', 'r')
        authors = json.loads(database.read())
        for author in authors:
            if author['id'] == id:
                return author
        return 'No author with id', id, 'exists in the database'
    
    @classmethod
    def create_author(self,name, lastname, nationality):
        database = open(r'src\data\authors.json', 'r+')
        authors = json.loads(database.read())
        new_author = {
            "id": len(authors)+1,
            "name":name,
            "last_name":lastname,
            "nationality":nationality
        }
        authors.append(new_author)
        database.seek(0)
        json.dump(authors,database,indent=4)

        res = "Created new author: " + str(new_author)

        return res
    
    @classmethod
    def update_author(self,id,name,last_name,nationality):
        database = open(r'src\data\authors.json', 'r+')
        authors = json.loads(database.read())
        new_data = []
        updated_author = {}
        for author in authors:
            if author['id'] == id:
                updated_author = author
                author['name'] = name
                author['last_name'] = last_name
                author['nationality'] = nationality
            new_data.append(author)
        if updated_author != {}:
            database.seek(0)
            json.dump(new_data,database,indent=4)
            return updated_author
        else:
            return 'No author exists with the given id'
        
    @classmethod
    def delete_author(self,id):
        # Regla de negocio: No permitir la eliminación de un autor si tiene libros asociados
        books_database = open(r'src\data\books.json', 'r')
        books = json.loads(books_database.read())
        books_database.close() # Buena práctica cerrar el archivo después de leerlo

        for book in books:
            if book['author_id'] == id:
                return f"Cannot delete author with id {id}: They have associated books."

        # Si no se encontraron libros, proceder con la eliminación
        database = open(r'src\data\authors.json', 'r+')
        authors = json.loads(database.read())
        
        author_to_delete = None
        for author in authors:
            if author['id'] == id:
                author_to_delete = author
                break
        
        if not author_to_delete:
            database.close()
            return f"Author with id {id} not found"

        authors.remove(author_to_delete)

        # Re-indexar IDs
        for i, author in enumerate(authors):
            author['id'] = i + 1
        
        database.seek(0)
        database.truncate()
        json.dump(authors, database, indent=4)
        database.close()
        return f"Author with id {id} has been deleted."