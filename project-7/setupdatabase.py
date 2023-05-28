from basic import db, Puppy

# Creates all the Tables Model
db.create_all()

sam = Puppy('Sammy', 3)
frankie = Puppy('Frankie', 4)

print(sam.id)

db.session.add_all([sam, frankie])

db.session.commit()

print(sam.id)