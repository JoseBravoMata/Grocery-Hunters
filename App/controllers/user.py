from flask import redirect, render_template, request, session, url_for
from flask_jwt import JWT, jwt_required, current_identity
from sqlalchemy.exc import IntegrityError

from App.models import ( db, User )

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
    id=len(User.query.all())
    newuser = User(id=id, firstname=userdata['firstname'],lastname=userdata['lastname'], email=userdata['email']) # create user object
    newuser.set_password(userdata['password']) # set password
    try:
        db.session.add(newuser)
        db.session.commit() # save user
    except IntegrityError: # attempted to insert a duplicate user
        db.session.rollback()
        return False # error message
    return True # success

def addRecipe(recipe):
    lid=len(MyRecipe.query.filter_by(id=current_identity).all())
    myRecipe=MyRecipe(id=current_identity, lid=lid)