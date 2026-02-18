from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")


@app.route("/alumnos")
def alumnos():
	return render_template("alumnos.html")

@app.route("/404")
def alumnos():
	return render_template("404.html")

if __name__ == '__main__':
	app.run(debug=True)

