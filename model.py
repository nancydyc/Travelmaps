from flask_sqlalchemy import SQLAlchemy

# Instantiate a SQLAlchemy object
db = SQLAlchemy()

class User(db.Model):
    """Data model for a user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, 
                        primary_key=True, 
                        autoincrement=True)
    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(25), nullable=False)

    def __repr__(self):
        """Return a human-readable representation of a user"""

        return f"<User user_id={self.user_id} fname={self.fname} lname={self.lname} email={self.email}>"

class Map(db.Model):
    """Data model for a map."""

    __tablename__ = "maps"

    map_id = db.Column(db.Integer, 
                        primary_key=True,   
                        autoincrement=True)
    user_id = db.Column(db.Integer, 
                        db.ForeignKey('users.user_id'))
    map_name = db.Column(db.String(50), nullable=False)
    map_description = db.Column(db.String(100), nullable=True)

    #***********
    user = db.relationship("User", backref="maps")
    place = db.relationship("Place", backref="maps")
    #***********

    def __repr__(self):
        """Return a human-readable representation of a map"""

        return f"<Map map_id={self.user_id} user_id={self.user_id} map_name={self.map_name}>"


class Place(db.Model):
    """Data model for a place."""

    __tablename__ = "places"

    place_id = db.Column(db.Integer, 
                        primary_key=True, 
                        autoincrement=True)
    map_id = db.Column(db.Integer, 
                        db.ForeignKey('maps.map_id'))
    latitude = db.Column(db.String(50), nullable=False)
    longitude = db.Column(db.String(50), nullable=False)
    google_place_name = db.Column(db.String(100), nullable=False)


    def __repr__(self):
        """Return a human-readable representation of a place"""

        return f"<Place place_id={self.place_id} map_id={self.map_id} latitude={self.latitude} longitude={self.longitude} google_place_name={self.google_place_name}>"

class UserPlace(db.Model):
    """Data model for a userplace."""

    __tablename__ = "userplaces"

    userplaces_id = db.Column(db.Integer, 
                        primary_key=True, 
                        autoincrement=True)
    user_id = db.Column(db.Integer, 
                            db.ForeignKey('users.user_id'))
    place_id =  db.Column(db.Integer, 
                            db.ForeignKey('places.place_id'))
    place_notes = db.Column(db.String(200), nullable=True)

    #***********
    user = db.relationship("User", backref="userplaces")
    place = db.relationship("Place", backref="userplaces")
    #***********


    def __repr__(self):
        """Return a human-readable representation of a userplace"""

        return f"<UserPlace userplace_id={self.userplace_id} user_id={self.user_id} place_id={self.place_id} place_notes={self.place_notes}>"


def connect_to_db(app):
    """Connect the database to the Flask app"""

    # Configure to use the database.
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///travelmaps"
    app.config["SQLALCHEMY_ECHO"] = False
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print("Connected to DB.")




