import os
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

app.config["MAX_CONTENT_LENGTH"] = 4196 * 4196
app.config["UPLOAD_EXTENSIONS"] = [".csv"]
app.config["UPLOAD_PATH"] = "uploads"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/index')
def redirect_index():
    return redirect(url_for("index"))


@app.route('/wrong-file')
def wrong_file():
    return render_template("wrongfile.html")


@app.route('/', methods=["POST"])
def upload_file():
    uploaded_file = request.files["file"]
    filename = uploaded_file.filename
    if uploaded_file.filename != "":
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config["UPLOAD_EXTENSIONS"]:
            return redirect(url_for("wrong_file"))
        else:
            uploaded_file.save(os.path.join(app.config["UPLOAD_PATH"], "dataset.csv"))
            return redirect(url_for("select_algorithm"))
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
