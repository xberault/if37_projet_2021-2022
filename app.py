from flask import Flask
from flask import render_template
import convert

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/trad/<mot>')
def trad(mot=None):
    res = convert.convert(convert.extractWords(mot))
    return render_template('res.html', mot=mot, res=res)


if __name__ == '__main__':
    app.run()
