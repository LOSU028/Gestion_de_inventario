from flask import Flask, jsonify, request
from controllers import authors_Cont
app = Flask(__name__)


@app.route("/authors", methods=["GET"])
def get_authors():
    return authors_Cont.list_authors()

if __name__ == "__main__":
    app.run(debug=True)