from flask import Blueprint, redirect, render_template, request, jsonify, send_from_directory
from flask_jwt import JWT, jwt_required, current_identity

user_views = Blueprint('user_views', __name__, template_folder='../templates')

from App.controllers import *

@user_views.route('/main', methods=['GET'])
def get_user_page():
    return render_template('main.html')

@user_views.route('/products', methods=['GET'])
def get_products_page():
    return render_template('products.html')

@user_views.route('/list', methods=['GET'])
def get_list_page():
    return render_template('list.html')

@user_views.route('/search', methods=['GET'])
def get_search_page():
    return render_template('search.html')

@user_views.route('/signin', methods=['POST'])
def sign_user_in():
    if(sign_in()):
      return "Success"
    return "Couldn't sign in"

@user_views.route('/signup', methods=['POST'])
def sign_user_up():
    if(sign_up()):
      return "Success"
    return "Couldn't sign up"

@user_views.route('/signup', methods=['GET'])
def get_signup_page():
    return render_template("signup.html")
    