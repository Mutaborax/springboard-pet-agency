from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """ Create a Pet Model """

    __tablename__ = "pets"

    pet_code = db.Column(db.Integer, primary_key=True)
    pet_name = db.Column(db.Text, nullable=False)
    pet_species = db.Column(db.Text, nullable=False)
    pet_url = db.Column(db.Text, nullable=False)
    pet_age = db.Column(db.Integer)
    pet_notes = db.Column(db.Text, nullable=True)
    pet_available = db.Column(
        db.Boolean, nullable=False, default=True)

    def __repr__(self):
        return f"<Pet {self.pet_name}, {self.pet_species}, {self.pet_url}, {self.pet_age}, {self.pet_notes}, {self.pet_available}>"
