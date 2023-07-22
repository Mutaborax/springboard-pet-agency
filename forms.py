from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, URL, Optional, NumberRange, AnyOf


class AddPetForm(FlaskForm):
    name = StringField('Pet Name', [InputRequired()])
    species = SelectField('Species', choices=[
                          ('cat', 'Cat'), ('dog', 'Dog'), ('hamster', 'Hamster'), ('parrot', 'Parrot'), ('tortoise', 'Tortoise'), ('snake', 'Snake'), ('bird', 'Bird')], validators=[InputRequired()])
    photo_url = StringField('Photo URL', [Optional(), URL()])
    age = IntegerField('Age', [Optional(), NumberRange(min=0, max=30)])
    notes = StringField('Notes')


class EditPetForm(FlaskForm):
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    notes = TextAreaField('Notes', validators=[Optional()])
    available = BooleanField('Available')
