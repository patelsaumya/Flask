from models import db, Puppy, Owner, Toy

rufus = Puppy('Rufus')
fido = Puppy('Fido')

db.session.add_all([rufus, fido])
db.session.commit()

print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='Rufus').first()

peter = Owner('Peter', rufus.id)

toy1 = Toy('Chew Toy', rufus.id)
toy2 = Toy('Ball', rufus.id)

db.session.add_all([peter, toy1, toy2])
db.session.commit()

print(rufus)

rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)
rufus.report_toys()