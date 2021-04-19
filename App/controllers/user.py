from flask import redirect, render_template, request, session, url_for
from flask_jwt import JWT, jwt_required, current_identity

from App.models import ( User )

def check_logged():
    return current_identity

def sign_in():
  return True