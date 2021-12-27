from flask import Flask

app = Flask(__name__)


from .convert import convert_sentence

from . import convert, views


def serve():
    app.run(debug=True)

