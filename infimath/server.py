from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import markdown, yaml

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

##CREATE TABLE
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
# db.create_all()

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":

        hash_and_salted_password = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            username=request.form.get('username'),
            password=hash_and_salted_password,
        )
        db.session.add(new_user)
        db.session.commit()
        
        #Log in and authenticate user after adding details to database.
        login_user(new_user)
        
        return redirect(url_for("home"))

    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        
        #Find user by email entered.
        user = User.query.filter_by(username=username).first()
        
        #Check stored password hash against entered password hashed.
        if check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('home'))

    return render_template("login.html")

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/admin", methods=["GET", "POST"])
@login_required
def admin():
    if current_user.id == 1:
        if request.method == "POST":
    
            hash_and_salted_password = generate_password_hash(
                request.form.get('password'),
                method='pbkdf2:sha256',
                salt_length=8
            )
            new_user = User(
                username=request.form.get('username'),
                password=hash_and_salted_password,
            )
            db.session.add(new_user)
            db.session.commit()

            return redirect('/admin')

        else:
            users = User.query.order_by(User.id).all()
            return render_template("admin.html", users=users)
    else:
        redirect(url_for("home"))

@app.route("/")
@login_required
def home():
    return render_template("index.html")


@app.route("/linear-algebra")
@login_required
def show_course():
    return render_template("course.html")


@app.route("/abstract-algebra/<path:subpath>")
@login_required
def abstract_algebra(subpath):
    # Open the file and load the file
    with open('/Users/sandeepsuman/Programs/flask-test/test1/infimath//abstract-algebra/nav.yaml') as f:
        data = yaml.load(f, Loader=yaml.loader.SafeLoader)
    # files = os.listdir("./abstract-algebra")
    input_file = open("/Users/sandeepsuman/Programs/flask-test/test1/infimath/abstract-algebra/{}.md".format(subpath), mode="r", encoding="utf-8")
    text = input_file.read()
    content = markdown.markdown(text, extensions=['tables', 'pymdownx.arithmatex', 'pymdownx.magiclink', 'pymdownx.tasklist'])
    return render_template("linear.html", content=content, navigation=data)

if __name__ == '__main__':
    app.run(debug=True)