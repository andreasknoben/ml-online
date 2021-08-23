from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route("/success/<name>")
def success(name):
	return "Welcome {}".format(name)
	
@app.route("/login", methods = ["GET"])
def login():
	user = request.args.get("name")
	return redirect(url_for("success", name = user))
	
if __name__ == "__main__":
	app.run()
