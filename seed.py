from models import Pet
from app import app, db

with app.app_context():
    db.reflect()
    db.drop_all()
    db.create_all()

    # Add dummy data
    pet1 = Pet(pet_name="Fluffy", pet_species="cat", pet_age=2,
               pet_url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ffarm8.staticflickr.com%2F7568%2F15785724675_999435f19f_k.jpg&f=1&nofb=1&ipt=cd771196b0915dae723740a36dd508c9c28495e7b724ce33069acd817b7832c7&ipo=images", pet_available=True)
    pet2 = Pet(pet_name="Rex", pet_species="dog", pet_age=5,
               pet_url="https://cdn.wallpapersafari.com/13/51/Kd4LHG.jpg", pet_available=False)
    pet3 = Pet(pet_name="Pokie", pet_species="porcupine", pet_age=1,
               pet_url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F01%2F48%2F33%2F0148333b7dedda2cd08d44179c3b38a4.jpg&f=1&nofb=1&ipt=8dba439f317e9c752be499a6dcf092ff7d5529e69bc45175d837c5ca0df363e7&ipo=images", pet_available=True)

    db.session.add_all([pet1, pet2, pet3])
    db.session.commit()
