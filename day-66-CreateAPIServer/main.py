from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


# Cafe TABLE Configuration
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
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

        # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
def get_cafes_from_db():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    return all_cafes

@app.route("/random")
def get_random_cafe():
    random_cafe = random.choice(get_cafes_from_db())
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def get_all_cafe():
    all_cafes = get_cafes_from_db()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


@app.route("/search")
def get_location_cafe():
    loc = request.args.get("loc")
    all_cafe = db.session.execute(db.select(Cafe).where(Cafe.location == loc)).scalars().all()
    if not all_cafe:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at the location."})
    else:
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafe])


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def post_new_cafe():
    print("hello")
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"Success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def patch_cafe_price(cafe_id):
    # update_cafe = cafe = db.get_or_404(Cafe, cafe_id)
    update_cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    if update_cafe:
        update_cafe.coffee_price = request.args.get("new_price")
        db.session.commit()
        ## Just add the code after the jsonify method. 200 = Ok
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        # 404 = Resource not found
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def report_closed_cafe(cafe_id):
    if request.args.get("api-key") == "TopSecretAPIKey":
        closed_cafe = db.get_or_404(Cafe, cafe_id)
        if closed_cafe:
            db.session.delete(closed_cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error="Sorry, that's not allowed. Make sure you have the correct api-key"), 403


if __name__ == '__main__':
    app.run(debug=True)
