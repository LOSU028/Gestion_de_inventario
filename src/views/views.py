from flask import jsonify

def display_authors(authors):
    return jsonify(authors)