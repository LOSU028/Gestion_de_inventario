
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
        database = open(r'src\data\authors.json', 'r+')
        authors = json.loads(database.read())
        database2 = open(r'src\data\authors.json', 'w')
        database2.truncate()
        aux = []
        for author in authors:
            if author['id'] != id:
                aux.append(author)
        new_id = 0
        for author in aux:
            author['id'] = new_id + 1
            new_id =+ 1
        database.seek(0)
        print(aux)
        json.dump(aux,database,indent=4)
        return id