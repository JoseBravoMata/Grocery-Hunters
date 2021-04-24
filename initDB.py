from main import db, Products, app
import csv

db.create_all(app=app)

with open('./App/products.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter= ',')

    for row in reader:
        if row['no'] == '':
            row['no'] = None
        if row['products'] == '':
            row['products'] = None
        if row['brand'] == '':
            row['brand'] = None
        if row['price'] == '':
            row['price'] = None

            products = Products(
                no= row['no'],
                products= row['products'],
                brand= row['brand'],
                price= row['price']
            )
            db.session.add(products)
            db.session.commit()
print('Database Initialized!')
