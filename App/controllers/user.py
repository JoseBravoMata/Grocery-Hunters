from flask import redirect, render_template, request, session, url_for
from flask_jwt import JWT, jwt_required, current_identity
from sqlalchemy.exc import IntegrityError
import json

from App.models import ( db, User, MyRecipe )


def check_logged():
    return current_identity

def sign_in(userdata):
  email=userdata["email"]
  password=userdata["password"]
  #search for the specified user
  user = User.query.filter_by(email=email).first()
  #if user is found and password matches
  if user and user.check_password(password):
        return True
  return False

def sign_up(userdata):
    newuser = User( firstname=userdata['firstname'],lastname=userdata['lastname'], email=userdata['email']) # create user object
    newuser.set_password(userdata['password']) # set password
    try:
        db.session.add(newuser)
        db.session.commit() # save user
    except IntegrityError: # attempted to insert a duplicate user
        db.session.rollback()
        return False # error message
    return True # success

def addRecipe(recipe):
    user=User.query.filter_by(email=recipe["email"]).first()
    lid=len(MyRecipe.query.filter_by(id=user.id).all())
    ingredients=""
    for ingredient in recipe["ingredients"]:
        ingredients+=ingredient["text"]
        ingredients+=", "
    myRecipe=MyRecipe( id=user.id, lid=lid, rname=recipe["label"], calories=recipe["calories"], fat=recipe["digest"][0]["total"], ingredients=ingredients, done=False)
    db.session.add(myRecipe)
    db.session.commit() # save user
    return "Success" # success

def deleteRecipe(lid, data):
    user=User.query.filter_by(email=data["email"]).first()
    recipe=MyRecipe.query.filter_by(id=user.id, lid=lid).first()
    if recipe:
        db.session.delete(recipe)
        db.session.commit()
        return 'Success'
    return "Failure" 

def updateRecipe(lid, data):
    user=User.query.filter_by(email=data["email"]).first()
    recipe=MyRecipe.query.filter_by(id=user.id, lid=lid).first()
    if recipe:
        recipe.done = data['done']
        db.session.add(recipe)
        db.session.commit()
        return 'Success'
    return "Failure" 


def getMyRecipes(data):
    user=User.query.filter_by(email=data["email"]).first()
    recipes=MyRecipe.query.filter_by(id=user.id).all()
    recipes=[recipe.toDict() for recipe in recipes]
    return json.dumps(recipes) # success
