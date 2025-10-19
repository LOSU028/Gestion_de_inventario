from flask import Flask, jsonify, request
from controllers import authors_Cont
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

if __name__ == "__main__":
    app.run(debug=True)