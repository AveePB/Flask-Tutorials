from flask import Blueprint, request, jsonify, render_template
from models import User

authz_bp = Blueprint('authz_bp', __name__)

# Function to return website
@authz_bp.route('/', methods=['GET'])
def index(): 
    return render_template('index.html')

# Function to create users
@authz_bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    
    username = data.get('username')
    password = data.get('password')

    if (User.create(username, password)):
        return jsonify({'message': 'User successfully created'}), 201
    else:
        return jsonify({'error': 'User already exists'}), 409

# Function to validate user credentials
@authz_bp.route('/login', methods=['POST'])
def login_user(): 
    data = request.get_json()
    
    username = data.get('username')
    password = data.get('password')

    if (User.validateCredentials(username, password)):
        return jsonify({'message': 'User credentials are valid'}), 200
    else:
        return jsonify({'error': 'Data are invalid'}), 404