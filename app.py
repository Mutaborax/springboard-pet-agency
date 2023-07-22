from flask import Flask, request, render_template, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, Pet, connect_db
from flask import flash, url_for
from forms import AddPetForm, EditPetForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///Pet'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def home():
    """Show all pets"""
    animals = Pet.query.all()
    return render_template("home.html", animals=animals)


@app.route('/add', methods=["GET", "POST"])
def add_pet():
    form = AddPetForm()

    if form.validate_on_submit():
        pet = Pet(
            pet_name=form.name.data,
            pet_species=form.species.data,
            pet_url=form.photo_url.data or None,
            pet_age=form.age.data or None,
            pet_notes=form.notes.data or None,
            pet_available=True
        )
        db.session.add(pet)
        db.session.commit()

        return redirect('/')

    return render_template('add_pet.html', form=form)


@app.route('/edit/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.pet_url = form.photo_url.data or None
        pet.pet_notes = form.notes.data or None
        pet.pet_available = form.available.data
        db.session.add(pet)
        db.session.commit()
        # Changed from '/home.html' to url_for('home')
        return redirect(url_for('home'))
    else:
        return render_template('edit_pet.html', form=form, pet=pet)


if __name__ == '__main__':
    app.run(debug=True)
