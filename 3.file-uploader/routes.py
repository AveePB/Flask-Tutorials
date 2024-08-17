from flask import Blueprint, jsonify, send_file, render_template, request
from models import File
import os

files_bp = Blueprint('files_bp', __name__)

@files_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html', files=File.query.all())

@files_bp.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['upload-file']
    description = request.form.get('description')
    
    if (File.save(file, description)):
        return jsonify({"message": "File successfully uploaded!"}), 204
    else:
        return jsonify({"error": "Failed to upload the file!"}), 409
    
@files_bp.route('/delete/<int:file_id>', methods=['DELETE'])
def delete_file(file_id):
    File.delete(file_id)
    
    return jsonify({"message": "File successfully deleted!"}), 204

@files_bp.route('/download/<int:file_id>', methods=['GET'])
def download_file(file_id):
    file = File.query.get(file_id)

    if (file != None):
        file_path = os.path.join('uploads', file.name)

        return send_file(file_path, as_attachment=True, download_name=file.name
    )

    return jsonify({"error": "File not found!"}), 404

