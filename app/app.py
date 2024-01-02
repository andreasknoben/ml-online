import os
from flask import Flask, render_template, redirect, url_for, request
from funcs import data_statistics, get_algorithm_parms, run_classifier

app = Flask(__name__)

app.config["MAX_CONTENT_LENGTH"] = 4196 * 4196
app.config["UPLOAD_EXTENSIONS"] = [".csv"]
app.config["UPLOAD_PATH"] = "uploads"

filename = None
algorithm = None

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/index')
def redirect_index():
    return redirect(url_for("index"))


@app.route('/wrong-file')
def wrong_file():
    return render_template("wrongfile.html")


@app.route('/algorithm')
def select_algorithm():
    stats = data_statistics(filename)
    return render_template("select-algorithm.html", data=stats)

@app.route('/run')
def run_algorithm():
    alg_parms = get_algorithm_parms(algorithm)

    result = run_classifier(alg_parms,seed)["test_accuracy"]
    
    return render_template("run-algorithm.html", data=alg_parms, score=round(result,4))


@app.route('/', methods=["POST"])
def upload_file():
    uploaded_file = request.files["file"]
    global filename
    filename = uploaded_file.filename
    if uploaded_file.filename != "":
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config["UPLOAD_EXTENSIONS"]:
            return redirect(url_for("wrong_file"))
        else:
            uploaded_file.save(os.path.join(app.config["UPLOAD_PATH"], "dataset.csv"))
            return redirect(url_for("select_algorithm"))
    return redirect(url_for("index"))


@app.route('/algorithm', methods=["POST"])
def select_algorithm_form():
    global algorithm
    global seed

    algorithm = request.form.get('algorithm')
    seed = request.form.get('random-seed') # seed for both the train-test split and the algorithm

    # If no value is given, set seed to None. Otherwise, try to convert it to int,
    # and when it fails, it sets the seed to the joined ascii values of input.
    if seed == "":
        seed = None
    else:
        try:
            seed = int(seed)
        except ValueError:
            seed = int("".join([str(ord(i)) for i in "abc"]))

    return redirect(url_for("run_algorithm"))


if __name__ == "__main__":
    app.run(debug=True)
