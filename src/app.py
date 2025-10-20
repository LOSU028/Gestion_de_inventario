from flask import Flask, jsonify, request
from controllers import authors_Cont, books_Cont
from models import authors
app = Flask(__name__)



@app.route("/authors", methods=["GET"])
def get_authors():
    return authors_Cont.list_authors()

@app.route("/authors/<int:author_id>", methods = ["GET"])
def get_author_by_id(author_id):
    return authors_Cont.get_author_by_id(author_id)

@app.route("/authors", methods = ["POST"])
def create_author():
    data = request.get_json()
    name = data.get("name")
    last_name = data.get("last_name")
    nationality = data.get("nationality")
    res = authors.Author.create_author(name, last_name, nationality)
    return res,201

@app.route("/authors/<int:author_id>", methods = ["PUT"])
def update_author(author_id):
    data = request.get_json()
    name = data.get("name")
    last_name = data.get("last_name")
    nationality = data.get("nationality")
    return authors_Cont.update_author(author_id, name, last_name, nationality)

@app.route("/authors/<int:author_id>", methods=["DELETE"])
def delete_author(author_id):
    return authors_Cont.delete_Author(author_id)

@app.route("/books", methods=["GET"])
def get_books():
    return books_Cont.list_books()

@app.route("/books/<int:book_id>", methods=["GET"])
def get_book_by_id(book_id):
    return books_Cont.get_book_by_id(book_id)

@app.route("/books", methods=["POST"])
def create_book():
    data = request.get_json()
    return books_Cont.create_book(data), 201

@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    data = request.get_json()
    return books_Cont.update_book(book_id, data)

@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    return books_Cont.delete_book(book_id)

if __name__ == "__main__":
    app.run(debug=True)