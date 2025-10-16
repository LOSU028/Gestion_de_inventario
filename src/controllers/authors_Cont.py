import sys
sys.path.insert(0,"../models")

from models import authors
from flask import jsonify
def list_authors():
    return authors.Author.getAll()