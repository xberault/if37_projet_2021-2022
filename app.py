from flask import Flask

app = Flask(__name__)

from src import serve

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'



if __name__ == '__main__':
    serve()
