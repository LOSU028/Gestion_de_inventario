import sys
sys.path.insert(0,"../models")

from models import authors
from flask import jsonify
from views import views
def list_authors():
    authors_in_db = authors.Author.getAll()
    return views.display_authors(authors_in_db)

def get_author_by_id(id):
    author = authors.Author.getOne(id)
    return views.display_author(author,id)

def update_author(id,name,last_name,nationality):
    updated_author = authors.Author.update_author(id, name, last_name, nationality)
    return views.display_updated_author(id,updated_author)

def delete_Author(id):
    authors.Author.delete_author(id)
    return views.display_deleted_author(id)