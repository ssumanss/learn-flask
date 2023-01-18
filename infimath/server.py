from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/linear-algebra")
def show_course():
    return render_template("course.html")

if __name__ == '__main__':
    app.run(debug=True)