from flask import Flask, render_template, request
import requests

posts = requests.get("https://api.npoint.io/82e2ef3c5f8dfea3d3bd").json()

app = Flask(__name__)

@app.route("/")
def generate_home():
    return render_template("index.html", all_posts=posts)

@app.route("/about")
def generate_about():
    return render_template("about.html")

@app.route("/contact")
def generate_contact():
    return render_template("contact.html")

@app.route("/contact", methods=["POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])   
        print(data["message"])     
        return render_template("contact.html", msg_sent=True)

    return render_template("contact.html", msg_sent=False)






        


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == '__main__':
    app.run(debug=True)


