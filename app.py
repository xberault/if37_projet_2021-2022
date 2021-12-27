from flask import Flask

app = Flask(__name__)

from src import serve


if __name__ == '__main__':
    serve()
