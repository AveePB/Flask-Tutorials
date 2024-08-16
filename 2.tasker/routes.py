from flask import Blueprint, render_template, jsonify, request
from models import Task

tasks_bp = Blueprint('tasks_bp', __name__)

# Function to fetch page
@tasks_bp.route('/', methods=["GET"])
def index():
    return render_template('index.html', tasks=Task.get_all())

# Function to add tasks
@tasks_bp.route('/add', methods=["POST"])
def add():
    data = request.get_json()
    if (Task.create(data['content'])):
        return jsonify({'message': 'Successfully added a task'}), 204
    else:
        return jsonify({'error': 'Failed to add a task'}), 409

# Function to remove tasks
@tasks_bp.route('/remove/<int:task_id>', methods=["DELETE"])
def remove(task_id):
    Task.delete(task_id)
    return jsonify({'message': 'Successfully removed a task'}), 204