from flask import Flask

app = Flask(__name__)


from .convert import convert_sentence, FORME_COURTE, FORME_CONTRACTEE, FORME_DEFAULT, FORME_LONGUE

from . import convert, views



def serve():
    app.run(debug=True)

