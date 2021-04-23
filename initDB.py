from main import app
from models import db, Ingredients
import csv

db.create_all(app=app)

with open('products.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter= ',')

    for row in reader:
        if row['no'] == '':
            row['no'] = None
        if row['products'] == '':
            row['products'] = None
        if row['brand'] == '':
            row['brand'] = None
        if row['size'] == '':
            row['size'] = None
        if row['price'] == '':
            row['price'] = None

            ingrediants = Ingredients(
                no= row['no'],
                products= row['products'],
                products= row['brand'],
                products= row['size'],
                products= row['price']
            )
            db.session.add(item)
            db.session.commit()
print('database initialized!')
