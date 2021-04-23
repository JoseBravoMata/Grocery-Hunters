from main import app
from models import db, Products
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

            products = Products(
                no= row['no'],
                products= row['products'],
                brand= row['brand'],
                size= row['size'],
                price= row['price']
            )
            db.session.add(products)
            db.session.commit()
print('Database Initialized!')
