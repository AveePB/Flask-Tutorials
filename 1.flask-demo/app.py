from flask import Flask
from models import db
from routes import authz_bp

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

    # Initialize SQLAlchemy
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(authz_bp)

    with app.app_context():
        db.create_all()  # Create database tables

    return app

if (__name__ == '__main__'):
    app = create_app()
    app.run(debug=True)
