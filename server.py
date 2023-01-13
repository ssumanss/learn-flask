from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return r"<h1>Guess the number between 0 and 1.</h1><p><img src='https://media.giphy.com/media/xUn3CftPBajoflzROU/giphy-downsized-large.gif'/></p>"


import random
a = random.randint(0,9)
@app.route("/<int:num>")
def guess_number(num):
    print(a)
    if num < a:
        return "<h1>Your Guess is Low.</h1><p><img src='https://media.giphy.com/media/ky9vnG678kzD91TO3N/giphy.gif'/></p>"
    elif num > a:
        return "<h1>Your Guess is High.</h1><p><img src='https://media.giphy.com/media/ekNWOoLSdHQUUurKid/giphy.gif'/></p>"
    else:
        return "<h1>Your Guess is Right.</h1><p><img src='https://media.giphy.com/media/26tknCqiJrBQG6bxC/giphy.gif'/></p>"


if __name__ == '__main__':
    app.run(debug=True)