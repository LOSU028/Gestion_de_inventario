
import json
class Author:
    def __init__(self, name = None, last_name = None, nationality = None):
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
            tmp = Author(author['name'], author['last_name'], author['nationality'])
            aux = tmp.toJSON()
            result.append(json.loads(aux))
        return result