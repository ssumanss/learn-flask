from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def generate_form():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def receive_data():
    name = request.form["fname"]
    passwd = request.form["pwd"]
    return f"<h1>First Name is {name} and password is {passwd}.</h1>"

if __name__ == '__main__':
    app.run(debug=True)