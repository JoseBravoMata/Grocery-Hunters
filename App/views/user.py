from flask import Blueprint, redirect, render_template, request, jsonify, send_from_directory
from flask_jwt import JWT, jwt_required, current_identity

user_views = Blueprint('user_views', __name__, template_folder='../templates')

from App.controllers import (check_logged)

@user_views.route('/main', methods=['GET'])
def get_user_page():
    return render_template('main.html')