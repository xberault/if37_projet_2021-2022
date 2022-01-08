from flask import render_template
from . import convert_sentence, FORME_DEFAULT, app
import pytesseract
from PIL import Image
import io


@app.route("/", methods=["GET", "POST"])
def index():
    from flask import request

    if request.method == "POST":
        a_traduire = str()
        if request.files["file"].filename != "":
            image_data = request.files["file"].read()

            a_traduire = pytesseract.image_to_string(
                Image.open(io.BytesIO(image_data)), lang="fra"
            )

        elif "txt_genre" in request.form:
            a_traduire = request.form.get("txt_genre")

        traduction = convert_sentence(a_traduire, FORME_DEFAULT)

        # res = convert.convert(convert.extractWords(mot))
        return render_template(
            "index.html", a_traduire=a_traduire, traduction=traduction
        )
    elif request.method == "GET":
        return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")