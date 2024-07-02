from faker import Faker # type: ignore
from random import randint, choice
from datetime import date, timedelta
from app import db, Pet, app

app.app_context().push()

faker = Faker()

dogs = ['morris.jpg', 'Peaches.jpg', 'Martin.jpg', 'Bolt.jpg',
        'Princess.jpg', 'Rex.jpg', 'Cleopatra.jpg',
        'Rufus.jpg', 'Sparkles.jpg', 'Russia.jpg',
        'Lewis.jpg', 'Monty-the-pup.jpg']


dog_breeds = [
"Labrador Retriever", "German Shepherd", "Golden Retriever","Bulldog",
"Beagle", "Poodle", "Rottweiler", "Boxer", "Yorkshire Terrier",
"Dachshund", "Siberian Husky", "Great Dane", "Doberman Pinscher",
"Shih Tzu", "Chihuahua", "Pomeranian", "Maltese",
"Miniature Schnauzer", "Bernese Mountain Dog", "Cavalier King Charles Spaniel"
]

def add_random_dogs():
    for dog_image in dogs:
        name = dog_image.split('.')[0]
        breed = choice(dog_breeds)
        pet = Pet(
            pet_type="Dogs",
            name=name,
            breed=breed,
            weight=round(randint(3, 8) + faker.random.random(), 1),
            age=randint(1, 15),
            location=faker.city(),
            arrival_date=date.today() - timedelta(days=randint(0, 365)),
            adoption_fee=round(randint(20, 100) + faker.random.random(), 2),
            shelter_id=1,
            image_url=f"http://localhost:5000/static/images/{dog_image}"
        )
        db.session.add(pet)
        db.session.commit()
        print(f"Added {name} to the database with breed {breed}.")


if __name__ == "__main__":
    add_random_dogs()
