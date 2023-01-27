from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_migrate import Migrate
import markdown, yaml

db = SQLAlchemy()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

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
    linear_algebra = db.Column(db.Boolean, unique=False, default=True)
    abstract_algebra = db.Column(db.Boolean, unique=False, default=True)


with app.app_context():
    db.create_all() 

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
                # print(not user.linear_algebra)

            if request.form.get('username') is not None:
                hash_and_salted_password = generate_password_hash(
                    request.form.get('password'),
                    method='pbkdf2:sha256',
                    salt_length=8
                )
                new_user = User(
                    username=request.form.get('username'),
                    password=hash_and_salted_password,
                    linear_algebra=(request.form.get('linear_algebra') == 'on'),
                )
                db.session.add(new_user)
                db.session.commit()

            elif request.form.get("linear_algebra") is not None:
                print(request.form.getlist("linear_algebra"))
                user = User.query.get(request.form.get("linear_algebra"))
                user.linear_algebra = not user.linear_algebra
                db.session.commit()

            elif request.form.get("abstract_algebra") is not None:
                print(request.form.getlist("abstract_algebra"))
                user = User.query.get(request.form.get("abstract_algebra"))
                user.abstract_algebra = not user.abstract_algebra
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
    user = current_user
    return render_template("index.html", user=user)


# @app.route("/linear-algebra")
# @login_required
# def show_course():
#     if current_user.linear_algebra:
#         return render_template("course.html")
#     else:
#         return "You are not enrolled in the course. <strong>Contact administrator.</strong>"


@app.route("/abstract-algebra/<path:subpath>")
@login_required
def abstract_algebra(subpath):
    if current_user.abstract_algebra:
        # Open the file and load the file
        with open('abstract-algebra/nav.yaml') as f:
            data = yaml.load(f, Loader=yaml.loader.SafeLoader)
        # files = os.listdir("./abstract-algebra")
        input_file = open("abstract-algebra/{}.md".format(subpath), mode="r", encoding="utf-8")
        text = input_file.read()
        content = markdown.markdown(text, extensions=['tables', 'pymdownx.arithmatex', 'pymdownx.magiclink', 'pymdownx.tasklist'])
        return render_template("course.html", content=content, navigation=data)
    else:
        return "You are not enrolled in the course. <strong>Contact administrator.</strong>"
        
if __name__ == '__main__':
    app.run(debug=True)