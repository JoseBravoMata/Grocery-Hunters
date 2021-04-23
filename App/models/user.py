from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()
import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email=  db.Column(db.String, unique=True, nullable=False)
    password= db.Column(db.String, nullable=False)
    firstname =  db.Column(db.String, nullable=False)
    lastname =  db.Column(db.String, nullable=False)
    
    def toDict(self):
        return{
            'id': self.id,
            'email': self.email,
            'firstname': self.firstname,
            'lastname': self.lastname
        }
    
    #hashes the password parameter and stores it in the object
    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    #Returns true if the parameter is equal to the object's password property
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)
    
    #To String method
    def __repr__(self):
        return '<User {}>'.format(self.username)  


    

class MyRecipe(db.Model):
    rid = db.Column(db.Integer, primary_key=True)
    id= db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) #set id as a foreign key to user.id 
    lid= db.Column(db.Integer, nullable=False) #set userid as a foreign key to user.id 
    rname =  db.Column(db.String, nullable=False)
    calories=  db.Column(db.Integer, nullable=True)
    fat=  db.Column(db.Integer, nullable=True)
    ingredients= db.Column(db.String, nullable=False)
    done = db.Column(db.Boolean, nullable=False)
   
    def toDict(self):
        return{
            'rid': self.rid,
            'lid': self.lid,
            'rname': self.rname,
            'calories': self.calories,
            'fat': self.fat,
            'ingredients': self.ingredients,
            'done': self.done
        }
