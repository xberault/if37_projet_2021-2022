from flask import render_template
from . import convert_sentence
from . import app


@app.route('/', methods=['GET', 'POST'])
def index():
    from flask import request
    if request.method == 'POST':
        a_traduire = request.form.get('txt_genre') 
        traduction = convert_sentence(a_traduire)
            
        #res = convert.convert(convert.extractWords(mot))
        return render_template("index.html", a_traduire=a_traduire, traduction=traduction)
    elif request.method == 'GET':
        return render_template("index.html", traduction="get")
   
