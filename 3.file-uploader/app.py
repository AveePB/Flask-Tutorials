from flask import Flask
from models import db
from routes import files_bp
import os

def create_app():
    app = Flask(__name__)
    app.register_blueprint(files_bp)
  
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///files.db'
    app.config['UPLOAD_FOLDER'] = 'uploads'
    
    os.makedirs('uploads', exist_ok=True)
    db.init_app(app)
    
    with app.app_context():
        db.create_all()

    return app

if (__name__ == '__main__'):
    app = create_app()
    app.run()