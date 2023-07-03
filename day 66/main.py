from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func, select
from flask import jsonify

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

## HTTP GET - Read Record

@app.route("/random")
def random():
    random_cafe = db.session.execute(db.select(Cafe).order_by(func.random())).scalar()
    json_data = jsonify(cafe=random_cafe.to_dict())
    return json_data

@app.route("/all")
def all():
    all_cafes = db.session.execute(db.select(Cafe).order_by(Cafe.id)).scalars()
    json_data = jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
    return json_data

@app.route("/search")
def search():
    loc = request.args.get("loc").title()
    cafe_at_loc = db.session.execute(db.select(Cafe).where(Cafe.location == loc)).scalars()
    json_data = jsonify(cafes=[cafe.to_dict() for cafe in cafe_at_loc])

    if len(json_data.json["cafes"]) == 0:
        return jsonify({"error": {"Not found": "Sorry we don't have a cafe at that location"}})
    else:
        return json_data

## HTTP POST - Create Record

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        cafe = Cafe(
            name = request.form["name"],
            map_url = request.form["map_url"],
            img_url = request.form["img_url"],
            location = request.form["location"],
            seats = request.form["seats"],
            has_toilet = bool(request.form["has_toilet"]),
            has_wifi = bool(request.form["has_wifi"]),
            has_sockets = bool(request.form["has_sockets"]),
            can_take_calls = bool(request.form["can_take_calls"]),
            coffee_price = request.form["coffee_price"]
        )
        
        db.session.add(cafe)
        db.session.commit()
        return jsonify({"response": {"success": "Successfully added new cafe."}})
    return render_template("add.html")

## HTTP PUT/PATCH - Update Record

@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def patch(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    cafe.coffee_price = new_price
    db.session.commit()
    return jsonify({"response": {"success": "Successfully updated the price"}})


## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
