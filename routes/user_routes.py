from flask import Blueprint, request, jsonify
from models.user_model import User
from config import db

user_bp = Blueprint('user_bp', __name__)

#GET obtener todos los usuarios
@user_bp.route('/users', methods={'GET'})
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])