from flask import Blueprint, render_template, jsonify, send_from_directory
import os

stream_bp = Blueprint('stream_bp', __name__)

@stream_bp.route('/')
def index():
    return render_template('index.html', short_names=['informations.mp4', 'neural-networks.mp4', 'social-media.mp4'])

@stream_bp.route('/stream/<short_name>')
def stream_short(short_name):
    if (os.path.exists(f'static/mp4/{short_name}')):
        return send_from_directory('static/mp4', short_name), 200
    else:
        return jsonify({'error': 'This mp4 file doesn\'t exist!'}), 404