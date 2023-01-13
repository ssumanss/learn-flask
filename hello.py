from flask import Flask

app = Flask(__name__)

def make_bold(func):
    def wrapper_function():
        return "<b>" + func() + "</b>"

    return wrapper_function

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
@make_bold
def say_bye():
    return "Bye"

@app.route("/username/<myname>")
def user_hello(myname):
    return f"Hello there { myname }"




if __name__ == '__main__':
    app.run(debug=True)