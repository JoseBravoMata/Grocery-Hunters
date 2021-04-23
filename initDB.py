from main import app
from models import db, Ingredients
import csv

db.create_all(app=app)

with open('ingrediants.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter= ',')

    for row in reader:
        if row['item'] == '':
            row['item'] = None
        if row['price'] == '':
            row['price'] = None

            ingrediants = Ingredients(
                item= row['item'],
                price= row['price']
            )
            db.session.add(item)
            db.session.commit()
print('database initialized!')