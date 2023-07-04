from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB.

# with app.app_context():
#     db.create_all()



@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        new_user = User(
            email = request.form.get("email"),
            password = generate_password_hash(request.form.get("password"), "pbkdf2", 8),
            name = request.form.get("name")
        )
        
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        return redirect(url_for("secrets"))
        
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = db.session.execute(db.select(User).filter_by(email=email)).scalar()

        if check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("secrets", name=user.name))
        else:
            flash("Email or Password is wrong, please try again.")
            return render_template("login.html")

    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    user = current_user
    return render_template("secrets.html", user=user)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/download', methods=["GET"])
@login_required
def download():
    return send_from_directory("./static/files/", "cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
